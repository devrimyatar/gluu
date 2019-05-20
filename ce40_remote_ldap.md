# CE4.0 with Remote LDAP

## Prepare LDAP Server
### Install Java

 - on CentOS7:
  `yum install java-11-openjdk`
 - on Ubuntu 16:
  `apt-get install default-jre`

### Install OpenDJ
```
wget https://ox.gluu.org/maven/org/forgerock/opendj/opendj-server-legacy/3.0.1.gluu/opendj-server-legacy-3.0.1.gluu.zip -O /opt/opendj-server-3.0.1.gluu.zip
cd /opt/
unzip /opt/opendj-server-3.0.1.gluu.zip
wget https://raw.githubusercontent.com/GluuFederation/community-edition-setup/master/static/opendj/101-ox.ldif -O /opt/opendj/template/config/schema/101-ox.ldif
wget https://raw.githubusercontent.com/GluuFederation/community-edition-setup/master/static/opendj/77-customAttributes.ldif -O /opt/opendj/template/config/schema/77-customAttributes.ldif
wget https://raw.githubusercontent.com/GluuFederation/community-edition-setup/master/static/opendj/96-eduperson.ldif -O /opt/opendj/template/config/schema/96-eduperson.ldif
```

Write the following content to `/opt/opendj/setup.properties`, befor running installation do not forget to change `hostname` and `rootUserPassword`:


```
hostname                        =c2.gluu.org
rootUserPassword            	   =VerySecretPassword

##### do not change below this line #######
ldapPort                        =389
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

## Install CE-4.0
Download latest CE-4.0 from https://repo.gluu.org/# and install with package manager:

- on CentOS7
  `rpm -i gluu-server-4.0-1-41.centos7.x86_64.rpm`
- on Ubuntu16
  `dpk -i gluu-server-4.0_1-48~xenial+Ub16.04_amd64.deb`
  
 Start container and login to container. Download latest setup.py from github:
 `wget https://raw.githubusercontent.com/GluuFederation/community-edition-setup/master/setup.py -O /install/community-edition-setup/setup.py`
 Execute with `--remote-ldap` option:
 `python /install/community-edition-setup/setup.py --remote-ldap`
 setup.py will ask you ldap server host and password, for example:
 ```
 Enter maximum RAM for applications in MB [3072] : 
    Ldap hostname : c2.gluu.org
    Password for 'cn=directory manager' : VerySecretPassword
```
 
