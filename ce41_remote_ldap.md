# CE4.1 with Remote LDAP

## Prepare LDAP Server
### Install Java

 - on CentOS7:
  `yum install java-11-openjdk`
 - on Ubuntu 16:
  `apt-get install default-jre`

### Install OpenDJ
```
wget https://ox.gluu.org/maven/org/forgerock/opendj/opendj-server-legacy/4.0.0-M3/opendj-server-legacy-4.0.0-M3.zip -O /opt/opendj-server-legacy-4.0.0-M3.zip
cd /opt/
unzip /opt/opendj-server-legacy-4.0.0-M3.zip
wget https://raw.githubusercontent.com/GluuFederation/community-edition-setup/version_4.0.1/static/opendj/101-ox.ldif -O /opt/opendj/template/config/schema/101-ox.ldif
wget https://raw.githubusercontent.com/GluuFederation/community-edition-setup/version_4.0.1/static/opendj/77-customAttributes.ldif -O /opt/opendj/template/config/schema/77-customAttributes.ldif
wget https://raw.githubusercontent.com/GluuFederation/community-edition-setup/version_4.0.1/static/opendj/96-eduperson.ldif -O /opt/opendj/template/config/schema/96-eduperson.ldif
```

Write the following content to `/opt/opendj/setup.properties`, befor running installation do not forget to change `hostname` and `rootUserPassword`:


```
hostname                        =c2.gluu.org
rootUserPassword                =VerySecretPassword

##### do not change below this line #######
generateSelfSignedCertificate   =true
enableStartTLS                  =false
ldapsPort                       =1636
adminConnectorPort              =4444
rootUserDN                      =cn=directory manager
baseDN                          =o=gluu
backendType                     =je
```

To rtart installation execute the following command

`/opt/opendj/setup --cli --propertiesFilePath /opt/opendj/setup.properties --acceptLicense --no-prompt`

## Install CE-4.1.0
Download latest CE-4.1.0 from https://repo.gluu.org/# and install with package manager:

- on CentOS7
  `rpm -i gluu-server-4.1.0-centos7.x86_64.rpm`
- on Ubuntu16
  `dpk -i gluu-server_4.1.0~xenial_amd64.deb`
- on Ubuntu18
  `dpk -i gluu-server_4.1.0~bionic_amd64.deb`
 
 Start container and login to container. To ensure we are using the same opendj version, download opendj:
  
 Execute setup.py with `--remote-ldap` option:
 
 `/install/community-edition-setup/setup.py --remote-ldap`
 
 
 setup.py will ask you ldap server host and password, for example:
 
 ```
 Enter maximum RAM for applications in MB [3072] : 
    LDAP hostname : c2.gluu.org
    Password for 'cn=directory manager' : VerySecretPassword
```
 
