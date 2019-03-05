import sys
import string
import uuid
import json
import random
from ldap3 import Server, Connection, MODIFY_REPLACE, MODIFY_ADD, MODIFY_DELETE, SUBTREE, ALL, BASE, LEVEL
import crypt
import sha
import os
import hashlib
import bcrypt
import time

if os.path.exists('gluu_people.txt'):
    os.rename('gluu_people.txt', 'gluu_people.txt.'+time.ctime().replace(' ','_'))

N = 120
bind_dn = 'cn=directory manager,o=gluu'
bind_pw = 'Gluu1234'
ldap_host = 'localhost'



server = Server('ldaps://'+ldap_host+':1636')

conn = Connection(server, bind_dn, bind_pw)
conn.bind()


conn.search('o=gluu', '(objectClass=*)', LEVEL)

for r in conn.response:
    if r['dn'].startswith('o='):
        dn=r['dn']
        inum = dn.split(',')[0][2:]
        
        
print "inumOrg", inum


first_names = json.load(open('first-names.json')) 
names = json.load(open('names.json')) 

domain_list = ('@gluu.org','@foo.org', '@mail.com', '@google.com', '@egg.org', '@yahoo.com', '@hotmail.com',
              '@linux.org', '@python.org', '@gnu.org', '@perl.net', '@php.net', '@something.net',
              '@nothing.org', '@this.net', '@my.net', '@you.org', '@tell.me', '@send.to', '@acme.foo.org',
              '@test.gluu.org', '@dev.gluu.org'
              )
def make_secret(password):
    """
    Encodes the given password as a base64 SSHA hash+salt buffer
    """
    salt = os.urandom(4)

    # hash the password and append the salt
    sha = hashlib.sha1(password)
    sha.update(salt)

    # create a base64 encoded string of the concatenated digest + salt
    digest_salt_b64 = '{}{}'.format(sha.digest(), salt).encode('base64').strip()

    # now tag the digest above with the {SSHA} tag
    tagged_digest_salt = '{{SSHA}}{}'.format(digest_salt_b64)

    return tagged_digest_salt

def bcrypt_password(password):
    return '{BCRYPT}' + bcrypt.hashpw(password, bcrypt.gensalt())

w = open('gluu_people.txt','a')

i = 0
while i < N :
    uid = str(uuid.uuid4()).upper()
    name = random.choice(first_names)
    sn = random.choice(names)
    dne = uid.split('-')[0]+'.'+uid.split('-')[-1]
    
    dn="inum={0}!0000!{1},ou=people,o={0},o=gluu".format(inum, dne)

    username = name+'.'+sn+ random.choice(domain_list)

    cn = name + ' ' + sn


    try:
        attributes={
             'objectClass': ['top', 'gluuPerson'],
             'givenname': name,
             "cn": cn,
             'sn': sn,
             'uid': username,
             'inum': '{0}!0000!{1}'.format(inum, dne),
             'gluustatus': 'active',
             'userpassword': bcrypt_password(str(sn)),
             'mail': username,
             'displayname': cn,
             'givenname': name,
             'iname': '*person*'+dne,
             'oxcreationtimestamp': '201902141656.114Z',
             'oxtrustemail': '{"operation":null,"value":"%s","display":"%s","primary":true,"reference":null,"type":"other"}'%(username,username)
             
            }

                
        r = conn.add(dn, attributes=attributes )
        if r:
    	    print r, i+1, username
    	    w.write(username+'\n')
    	else:
    	    print conn.response

        i += 1
    except:
	print "error"
	print conn.result
    
w.close()
