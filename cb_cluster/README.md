# Requirements
* two VM for couchbase clusterd, in our case they are c1.gluu.org and c2.gluu.org, they are both CentOS7
* one VM for gluu-4.0, in our case it is c3.gluu.org, Ubuntu16

# Installing couchbase servers
## Node1:
I choose c2.gluu.org as node 1. Simply execute the following command 

```
# rpm -i couchbase-server-enterprise-6.0.1-centos7.x86_64.rpm
```

After installation, I visit http://c2.gluu.org:8091/ to setup cluster

(setup_cb_node1_1.png)