#!/usr/bin/python

import requests
import os
import json
import cgi

oxd_id = '3ab0a2d8-0b81-4908-8c4f-8418e69046e1'
client_secret = 'eddf7f30-4d68-4d3e-9313-a7c2a97fdd76'
client_id = '@!5856.8A6C.09D4.C454!0001!655A.E96C!0008!7CCD.CDD4.4E84.6F81'
oxd_server = 'https://c3.gluu.org:8443/'
op_host = "https://c2.gluu.org"

print 'Content-type: text/html'


def post_data(end_point, data, access_token):
    """Posts data to oxd server"""
    headers = {
                'Content-type': 'application/json', 
                'Authorization': "Bearer " + access_token
        }

    result = requests.post(
                    oxd_server + end_point, 
                    data=json.dumps(data), 
                    headers=headers, 
                    verify=False
                    )

    return result.json()

# We will use PATH_INFO which URI is requested
path_info = os.environ.get('PATH_INFO','/')

#If login is requested
if path_info.startswith('/login'):
    print
    args = cgi.parse_qs(os.environ[ "QUERY_STRING" ])
    
    # Read access_token that we previously saved
    oxd_access_token = open('/tmp/oxd_access_token.txt').read()

    data = {
        "oxd_id": oxd_id,
        "code": args['code'][0],
        "state": args['state'][0]
    }

    # [4] Request access token to retreive user info. If you don't need user info
    # It is enough to make sure the user logged in
    result = post_data('get-tokens-by-code', data, oxd_access_token)

    data = {
        "oxd_id": oxd_id,
        "access_token": result['access_token']
    }

    # [5] Now we can retreive user information.
    result = post_data('get-user-info', data, oxd_access_token)
    
    # Finally print user info
    for cl in result['claims']:
        print '<br><b>{0} :</b> {1}'.format(cl, result['claims'][cl][0])
    
    print '<br><a href="/logoutme">Click here to logout</a>'

#If user wants to logout, he should first come to this pasge
elif path_info.startswith('/logoutme'):

    data = {
        "oxd_id": oxd_id,
    }

    # [6] Request logout uri from oxd server.
    result = post_data('get-logout-uri', data, oxd_access_token)

    
    # print redirection headers
    print "Status: 303 Redirecting"
    print "Location: "+ result['uri']
    print

# User will be redirected after logging out
elif path_info.startswith('/logout'):
    print
    print "logged out"

else:
    print
    # [2] We need to get access_token from oxd-server
    data = {
      "op_host": op_host,
      "scope": ["openid","oxd", "profile"],
      "client_id": client_id,
      "client_secret": client_secret,
      "authentication_method": "",
      "algorithm": "",
      "key_id": ""
    }

    result = post_data('get-client-token', data, '')
    oxd_access_token = result['access_token']

    # Since cgi scripts runs per request, we need access_token in subsequent queries.
    # Thus write a file. access_token should be secured and better to use session
    # in web frameworks.
    with open('/tmp/oxd_access_token.txt','w') as W:
        W.write(oxd_access_token)

    data = {
      "oxd_id": oxd_id,
      "scope": ["openid", "profile"],
      "acr_values": [],
    }

    # [3] User will be directed to Gluu Server to login, so wee need an url for login
    result = post_data('get-authorization-url', data, oxd_access_token)

    print '<a href="{0}">Click here to login</a>'.format(result['authorization_url'])
