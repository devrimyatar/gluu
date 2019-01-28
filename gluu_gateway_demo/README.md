# Gluu Gateway Demo Flask Application

Requirements
============
For this demo I will use the following VM's.

|IP Address      |Hosts            |OS                                |
|----------------|-----------------|----------------------------------|
|192.168.56.1    |rs.mygluu.org    |Any OS on which Python/flask runs |
|192.168.56.102  |op.mygluu.org    |Any Linux supported by Gluu Server|
|192.168.56.104  |gg.mygluu.org    |Currently I use Ubuntu 16.04 LTS  |
|192.168.56.101  |claim-gatering.mygluu.org, none-claim-gatering.mygluu.org | Any OS on which Python/flask runs|


Since I am using virtual IP/hosts I write the following content to file `/etc/hosts` on each machine

```
192.168.56.1 rs rs.mygluu.org
192.168.56.102 op op.mygluu.org
192.168.56.104 gg gg.mygluu.org
192.168.56.101 claim-gatering.mygluu.org
192.168.56.101 none-claim-gatering.mygluu.org

```



![Sample Screenshot](gg_demo_scrren_shot.png)
