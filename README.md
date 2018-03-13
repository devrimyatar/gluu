# Custom files for Gluu servers
This repo contains some binary files for Gluu servers and self testing scripts before publishin on the official site

Upgrade Gluu Server 2.4.x to 3.1.2
============================================

Export the data from the current installation
----------------------------------------------
```
# service gluu-server-2.x.x login
# wget https://raw.githubusercontent.com/GluuFederation/community-edition-setup/master/static/scripts/export2431.py
# wget -c https://raw.githubusercontent.com/GluuFederation/community-edition-setup/master/ldif.py
# curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"
# python get-pip.py
# pip install jsonmerge
# python export2431.py
```

Install the latest version of the Gluu server (ubuntu 16)
----------------------------------------------------------
```
# cp backup_2431/setup.properties /install/community-edition-setup
# cd install/community-edition-setup
# ./setup.py
# apt-get update
# apt-get install -y python-pip python-ldap
# pip install jsonmerge
# wget https://raw.githubusercontent.com/mbaser/gluu/master/import2431.py
# wget https://raw.githubusercontent.com/GluuFederation/cluster-mgr/master/testing/ldifschema_utils.py
# python import2431.py backup_2431
```

Install the latest version of the Gluu server (Centos7.x)
----------------------------------------------------------
```
# cp backup_2431/setup.properties /install/community-edition-setup
# cd install/community-edition-setup
# ./setup.py
# yum install epel-release
# yum clean all
# yum install python-ldap
# curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"
# python get-pip.py
# pip install jsonmerge
# wget https://raw.githubusercontent.com/mbaser/gluu/master/import2431.py
# wget https://raw.githubusercontent.com/GluuFederation/cluster-mgr/master/testing/ldifschema_utils.py
# python import2431.py backup_2431/
```
