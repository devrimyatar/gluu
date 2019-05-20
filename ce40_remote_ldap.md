# CE4.0 with Remote LDAP


## Install Java

 - on CentOS7:
  `yum install java-11-openjdk`
 - on Ubuntu 16:
  `apt-get install default-jre`

## Install OpenDJ
```
cd /opt
wget https://ox.gluu.org/maven/org/forgerock/opendj/opendj-server-legacy/3.0.0.1.gluu/opendj-server-legacy-3.0.0.1.gluu.zip
unzip opendj-server-legacy-3.0.0.1.gluu.zip
wget https://raw.githubusercontent.com/GluuFederation/community-edition-setup/master/static/opendj/101-ox.ldif -O /opt/opendj/template/config/schema/101-ox.ldif
wget https://raw.githubusercontent.com/GluuFederation/community-edition-setup/master/static/opendj/77-customAttributes.ldif -O /opt/opendj/template/config/schema/77-customAttributes.ldif
wget https://raw.githubusercontent.com/GluuFederation/community-edition-setup/master/static/opendj/96-eduperson.ldif -O /opt/opendj/template/config/schema/96-eduperson.ldif
```

Write the following content to `/opt/opendj/setup.properties`, befor running installation do not forget to change `hostname` and `rootUserPassword`:


```
hostname                        =<hostname of ldap server>
rootUserPassword            	=<password for cn=directory manager>

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

`/opt/opendj/setup --cli --propertiesFilePath /opt/opendj/wrends.properties --acceptLicense --no-prompt`

