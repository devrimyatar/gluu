@moabu Here is how to migarte ldap to mysql
# ldap2mysql Migration

1) Setup a MySQL Server that is accessible remotely
  - Create a database for Gluu Server
  - Create a user that have all previleges of the database

2) Upgrade 4.x server to 4.3.1
  - Download https://raw.githubusercontent.com/GluuFederation/community-edition-package/master/update/4.3.1/upg4xto431.py
  - Execute upgrade script: `gldev=true python3 upg4xto431.py`

3) Migrate to MySQL
  - Copy script to setup root: `cp /install/community_edition_setup_4.3.1/static/scripts/ldap2mysql.py /install/community_edition_setup_4.3.1`
  - Exceute migration script as
    `python3 /install/community_edition_setup_4.3.1/ldap2mysql.py -rdbm-user=<mysql user> -rdbm-password=<mysql user passwrod> -rdbm-db=<mysql database> -rdbm-host=<mysql host>`
