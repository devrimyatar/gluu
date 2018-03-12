# Custom files for Gluu servers
This repo contains some binary files for Gluu servers and self testing scripts before publishin on the official site

Upgrade Gluu Server 2.4.x to 3.1.2
============================================

apt-get update
apt-get install -y python-pip python-ldap
pip install jsonmerge
wget https://raw.githubusercontent.com/mbaser/gluu/master/import2431.py
wget https://raw.githubusercontent.com/GluuFederation/cluster-mgr/master/testing/ldifschema_utils.py
python import2431.py backup_2431
