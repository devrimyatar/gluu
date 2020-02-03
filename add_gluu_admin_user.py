import sys
import uuid
import ldap
import ldap.modlist as modlist
import os
import hashlib

ldap.set_option(ldap.OPT_X_TLS_REQUIRE_CERT, ldap.OPT_X_TLS_ALLOW)


admin_user = raw_input('New admin username:')
admin_pw = raw_input('Admin password:')


for l in open('/etc/gluu/conf/gluu-ldap.properties'):
    ls = l.strip()
    if ls.startswith('bindPassword:'):
        n = ls.find(':')
        pwe = ls[n+1:]
        bind_pw  = os.popen('/opt/gluu/bin/encode.py -D ' + pwe).read().strip()


bind_dn = 'cn=directory manager'
ldap_host = 'localhost'


conn = ldap.initialize('ldaps://{0}:1636'.format(ldap_host))
conn.simple_bind_s(bind_dn, bind_pw)

result = conn.search_s('ou=groups,o=gluu',ldap.SCOPE_SUBTREE, ('gluuGroupType=gluuManagerGroup'))

admin_dn = result[0][0]




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



admin_pw_e = make_secret(admin_pw)

inum = str(uuid.uuid4())

entry = {
             'objectClass': ['top', 'gluuPerson'],
             'givenname': admin_user,
             "cn": admin_user,
             'sn': admin_user,
             'uid': admin_user,
             'inum': str(uuid.uuid4()),
             'gluustatus': 'active',
             'userpassword': admin_pw_e,
             'mail': admin_user+'@foo.org',
             'displayname': admin_user,
             'givenname': admin_user,
             'memberOf': admin_dn,
}

dn = 'inum={},ou=people,o=gluu'.format(inum)
ldif = modlist.addModlist(entry)
conn.add_s(dn, ldif)

conn.modify_s(admin_dn, [( ldap.MOD_ADD, 'member',  dn)])
