import sys
import string
import uuid
import json
import random
import os
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from requests.auth import HTTPBasicAuth

try:
    requests.packages.urllib3.disable_warnings()
except:
    pass

import sha
import os
import hashlib
import time

if os.path.exists('gluu_people.txt'):
    os.rename('gluu_people.txt', 'gluu_people.txt.'+time.ctime().replace(' ','_'))

N = 1
admin_user = 'admin'
admin_pw = 'XXXXXXXX'
cb_host = 'c1.gluu.org'


class CBM:

    def __init__(self, host, admin, password, port=18091, n1qlport=18093):
        self.host = host
        self.port = port
        self.n1qlport = n1qlport
        self.auth = HTTPBasicAuth(admin, password)
        self.set_api_root()

    def set_api_root(self):
        self.api_root = 'https://{}:{}/'.format(self.host, self.port)
        self.n1ql_api = 'https://{}:{}/query/service'.format(self.host, self.n1qlport)


    def _post(self, endpoint, data):
        url = os.path.join(self.api_root, endpoint)
        result = requests.post(url, data=data, auth=self.auth, verify=False)
        return result
    
    def exec_query(self, query):
        data = {'statement': query}
        result = requests.post(self.n1ql_api, data=data, auth=self.auth, verify=False)

        return result




cbm = CBM(cb_host, admin_user, admin_pw)

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


w = open('gluu_people.txt','a')

i = 0
while i < N :
    i += 1
    inum = str(uuid.uuid4())
    name = random.choice(first_names)
    sn = random.choice(names)
    
    dn="inum={0},ou=people,o=gluu".format(inum)

    key = 'people_'+inum

    email = '{}.{}{}'.format(name, sn, random.choice(domain_list))


    cn = name + ' ' + sn


    user_data = {
              "userPassword": make_secret(sn),
              "mail": email,
              "displayName": cn,
              "givenName": name,
              "objectClass": [
                "top",
                "gluuPerson",
                "gluuCustomPerson",
                "eduPerson"
              ],
              "dn": dn,
              "cn": cn,
              "inum": inum,
              "uid": email,
              "gluuStatus": "active",
              "sn": sn
            }


    query = 'UPSERT INTO `gluu_user` (KEY, VALUE) VALUES ("{}", {})'.format(key, json.dumps(user_data))
    try:
        result = cbm.exec_query(query)
        if result.ok:
            i += 1
            print i, email
    except:
        print "Failed to add"
    

w.close()
