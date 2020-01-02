# Setting up oxd-server Cluster

In this tutorial we are going to setup oxd-server cluster with nginx load balancer on CentOS 7.
For this purpose we need 5 VMs. My VMs are as follows:

| Name          | Hostname          | IP address        |
| ------------- |-------------------| ------------------|
| Gluu Server   | op.mygluu.org     | 192.168.56.104    |
| Redis Server  | redis.mygluu.org  | 192.168.56.103    |
| Oxd Server 1  | oxd1.mygluu.org   | 192.168.56.101    |
| Oxd Server 2  | oxd2.mygluu.org   | 192.168.56.102    |
| Load Balancer | lb.mygluu.org     | 192.168.56.105    |


## Gluu Server [op.mygluu.org]

Install gluu server as described in https://www.gluu.org/docs/ce/4.0/installation-guide/install-centos/

## Redis Server [redis.mygluu.org]

Install redis server and stunnel

```
# yum clean all
# yum install -y epel-release
# yum install -y redis stunnel
```

Enable and start redis:

```
# systemctl enable redis.service
# systemctl start redis.service
```

Generate certificate for stunnel
```
# openssl req -x509 -nodes -days 3650 -newkey rsa:2048 -batch -keyout /etc/stunnel/redis-server.key -out /etc/stunnel/redis-server.crt
```

Combine `redis-server.key` and `redis-server.crt` to make `redis-server.pem` and set permissions

```
# cat /etc/stunnel/redis-server.key /etc/stunnel/redis-server.crt > /etc/stunnel/redis-server.pem
# chmod 600 /etc/stunnel/redis-server.key
# chmod 600 /etc/stunnel/redis-server.pem
```

We need to copy `redis-server.pem` to each oxd-server node.

Write the following content to `/etc/stunnel/stunnel.conf`

```
pid = /run/stunnel-redis.pid
cert = /etc/stunnel/redis-server.pem
[redis-server]
accept = redis.mygluu.org:16379
connect = 127.0.0.1:6379
```

Download stunnel-systemd script:

```
# wget https://raw.githubusercontent.com/liuliang/centos-stunnel-systemd/master/stunnel.service -O /lib/systemd/system/stunnel.service
```

Enable and start stunnel:

```
# systemctl enable stunnel.service
# systemctl start stunnel.service
```

## Oxd Server 1 & 2 [oxd1.mygluu.org and oxd2.mygluu.org]

Please repeat the following instructions on oxd1.mygluu.org and oxd2.mygluu.org

Install stunnel:

```
# yum clean all
# yum install -y epel-release
# yum repolist
# yum install -y stunnel
# wget https://raw.githubusercontent.com/liuliang/centos-stunnel-systemd/master/stunnel.service -O /lib/systemd/system/stunnel.service
```

Please download `/etc/stunnel/redis-server.pem` from **Redis Server** and upload to each **Oxd Server**.
Write the following content to `/etc/stunnel/stunnel.conf`:

```
pid = /run/stunnel-redis.pid
cert = /etc/stunnel/redis-server.pem
[redis-client]
client = yes
accept = 127.0.0.1:6379
connect = redis.mygluu.org:16379
```

Enable and start stunnel:

```
# systemctl enable stunnel.service
# systemctl start stunnel.service
```

Install java and oxd-server:

```
# yum -y install java-1.8.0-openjdk-headless
# yum install -y https://repo.gluu.org/centos/7/oxd-server-4.0-centos7.noarch.rpm
```

Set the followings on `/opt/oxd-server/conf/oxd-server.yml`

```
trust_all_certs: true

storage: redis
storage_configuration:
    servers: "localhost:6379"
    redisProviderType: STANDALONE


op_host: 'https://op.mygluu.org'

```

Start oxd-server:

```
systemctl start oxd-server
```

## Load Balancer [lb.mygluu.org]

Install nginx

```
# yum clean all
# yum install -y epel-release
# yum repolist
# yum install -y nginx
```

Create self signed certificate:

```
# openssl req -x509 -newkey rsa:4096 -nodes -out /etc/nginx/httpd.crt -keyout httpd.key -days 365
```

Modify `/etc/nginx/nginx.conf` as follows: 

```
events {
        worker_connections 6500;
}

http {

  upstream oxdserver {
  server oxd1.mygluu.org:8443 max_fails=2 fail_timeout=10s;
  server oxd2.mygluu.org:8443 max_fails=2 fail_timeout=10s;
  }

  server {
    listen 8443 ssl;
    server_name lb.mygluu.org;

    ssl_certificate         /etc/nginx/httpd.crt;
    ssl_certificate_key     /etc/nginx/httpd.key;

    location / {
      proxy_pass https://oxdserver;
    }

  }

}
```

Enable and start nginx:

```
# systemctl enable nginx.service
# systemctl start nginx.service
```
