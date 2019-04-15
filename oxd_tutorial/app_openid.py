#!/usr/bin/python

# Gluu Server OpenID authorization/authentication Flask Example
# Deployment:
# Intsall flask and python openid library: sudo pip install flask oic
# Create cert.pem and cert.key: openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365
# Set variables my_host, op_host, and contact below
# Run server: python python app_openid.py
# This will dynamically register client and save client info to  client.json
# Navigate to htts://<my_host>:20443
# where <my_host> is hostname of server on which this script is running


import os

from flask import Flask, request, redirect, url_for, session, json

from oic.oic import Client
from oic.utils.authn.client import CLIENT_AUTHN_METHOD
from oic import rndstr
from oic.oic.message import AuthorizationResponse
from oic.oic.message import RegistrationResponse


# Set these three variables:
my_host = 'c3.gluu.org' 
op_host = "https://c1.gluu.org"
contact = 'admin@gluu.org'


##### end of config #####

port = 20443
redirect_uri = 'https://{}:{}/login_callback'.format(my_host, port)


client = Client(client_authn_method=CLIENT_AUTHN_METHOD, verify_ssl=False)

provider_info = client.provider_config(op_host)

if os.path.exists('client.json'):
    client_info = json.loads(open('client.json').read())
else:
    # we need to register a client
    args = {'redirect_uris': [redirect_uri], 'contacts': [contact], "scope": ["openid","user_name","mail"]}
    registration_response = client.register(provider_info["registration_endpoint"], **args)
    client_info = dict(registration_response)
    json.dump(client_info, open('client.json','w'), indent=2)


client_id = client_info["client_id"]
info = {"client_id": client_info["client_id"], "client_secret": client_info["client_secret"]}
client_reg = RegistrationResponse(**info)
client.store_registration_info(client_reg)


app = Flask(__name__)
app.config['SECRET_KEY'] = 'change-this-secret-key'


@app.route('/')
def index():

    session["state"] = rndstr()
    session["nonce"] = rndstr()

    args = {
        "client_id": client_id,
        "response_type": "code",
        "scope": ["openid","user_name","mail"],
        "nonce": session["nonce"],
        "redirect_uri": redirect_uri,
        "state": session["state"]
        }

    auth_req = client.construct_AuthorizationRequest(request_args=args)
    login_url = auth_req.request(client.authorization_endpoint)

    return '<a href="{0}">Click here to login</a>'.format(login_url)


@app.route('/login_callback/')
def login():

    response = request.query_string
    aresp = client.parse_response(AuthorizationResponse, info=response, sformat="urlencoded")
    args = {"code": aresp["code"]}
    resp = client.do_access_token_request(state=aresp["state"], request_args=args, authn_method="client_secret_basic")
    userinfo = client.do_user_info_request(state=aresp["state"])
    
    html_ = '<table>'
    
    for ui in userinfo:
        html_ += '<tr><th>{}:</th><td>{}</td></tr>'.format(ui, userinfo[ui])
    
    html_ += '</table>'
    
    return html_



if __name__ == '__main__':
    app.debug=True
    app.run(host="0.0.0.0",ssl_context=('cert.pem', 'key.pem'), port=port)
