#!/usr/bin/python

# This is an example flask application that shows you how to use oauth2
# authorization/authentication using Gluu Server 3.1.4

from flask import Flask, request

from authlib.client import OAuth2Session

client_id='@!6687.F518.B5E3.74BE!0001!D89A.5530!0008!EC86.F218.742C.59AB'
client_secret="ff6aaae4-1035-43e8-923d-2d1adf1e7721"
scope = 'openid user_name'

op_host = 'https://c3.gluu.org'
me = 'https://c2.gluu.org:8080'

authorize_url = '{}/oxauth/restv1/authorize'.format(op_host)
account_url = '{}/oxauth/restv1/userinfo'.format(op_host)
access_token_url = '{}/oxauth/restv1/token'.format(op_host)
login_callback_uri='{}/login_callback'.format(me)
logout_callback_uri='{}/logout_callback'.format(me)

auth_session = OAuth2Session(client_id, client_secret, scope=scope)
auth_session.verify = False


app = Flask(__name__)
app.config['SECRET_KEY'] = 'change-this-secret-key'

@app.route('/')
def index():
    uri, state = auth_session.create_authorization_url(authorize_url)
    return '<a href="{0}">Click here to login</a>'.format(uri)

@app.route('/login_callback')
def login():
    token = auth_session.fetch_access_token(url=access_token_url, 
                authorization_response=request.url, redirect_uri=login_callback_uri)
    session = OAuth2Session(client_id, client_secret, token=token, scope=scope)
    resp = auth_session.get(account_url)
    claims = resp.json()
    session_state = request.args['session_state']
    id_token = token['id_token']
    #id_token = token['access_token']
    logout_url = '{}/oxauth/restv1/end_session?id_token_hint={}&session_state={}&post_logout_redirect_uri='.format(op_host, id_token, session_state, logout_callback_uri)
    return 'Welcome {0}. You can logout: <a href="{1}">{1}'.format(claims['user_name'], logout_url)

@app.route('/logout_callback')
def logout():
    return "logged out"


if __name__ == '__main__':
    app.debug=False
    app.run(host="0.0.0.0", ssl_context='adhoc', port=8080)
