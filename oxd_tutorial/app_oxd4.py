from flask import Flask, request, redirect, url_for, session, json
from flask_login import LoginManager, UserMixin, current_user, login_required, login_user, logout_user

import requests

oxd_id = 'a14a19c7-2b62-45b3-a1c3-ec486eb319ca'
client_secret = '1b5268a2-66b3-4797-be23-6a741be9720e'
client_id = '@!2A7E.034D.5BE2.F1D6!0001!8405.423D!0008!36F1.EE00.1832.90D8'
oxd_server = 'https://c3.gluu.org:8443/'
op_host = "https://c2.gluu.org"


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


app = Flask(__name__)
app.config['SECRET_KEY'] = 'change-this-secret-key'
login_manager = LoginManager()
login_manager.init_app(app)


class User(UserMixin):
    def __init__(self, username):
        self.username = username
        self.id = None

    def get_id(self):
        return self.username

@login_manager.user_loader
def load_user(username):
    user = User(username)
    return user


@app.route('/')
def index():

    data = {
      "op_host": op_host,
      "scope": ["openid","oxd", "profile", "user_name"],
      "client_id": client_id,
      "client_secret": client_secret,
      "authentication_method": "",
      "algorithm": "",
      "key_id": ""
    }

    result = post_data('get-client-token', data, '')
    oxd_access_token = result['access_token']

    session['access_token'] = oxd_access_token

    data = {
      "oxd_id": oxd_id,
      "scope": ["openid", "profile", "user_name"],
      "acr_values": [],
    }

    result = post_data('get-authorization-url', data, oxd_access_token)

    return '<a href="{0}">Click here to login</a>'.format(result['authorization_url'])


@app.route('/login')
def login():
    data = {
        "oxd_id": oxd_id,
        "code": request.args['code'],
        "state": request.args['state']
    }

    result = post_data('get-tokens-by-code', data, session['access_token'])

    data = {
        "oxd_id": oxd_id,
        "access_token": result['access_token']
    }

    result = post_data('get-user-info', data, session['access_token'])
    
    

    if result.get('claims') and result['claims'].get('sub'):
        user = User(result['claims']['user_name'][0])
        login_user(user)

        session['claims'] = result['claims']
        return redirect(url_for('welcome'))

    return 'Not authorized'

@app.route('/welcome')
@login_required
def welcome():

    ret_html = 'Welcome ' + current_user.username
    
    for cl in session['claims']:
        ret_html += '<br><b>{0} :</b> {1}'.format(cl, session['claims'][cl][0])
    
    ret_html += '<br><a href="/logoutme">Click here to logout</a>'
    
    return ret_html


@app.route("/logoutme")
@login_required
def logoutme():
    logout_user()

    data = {
        "oxd_id": oxd_id,
    }

    result = post_data('get-logout-uri', data, session['access_token'])
    session.clear()
    return redirect(result['uri'])


@app.route("/logout")
def logout():
    return "Logged out"


if __name__ == '__main__':
    app.debug=True
    app.run(host="0.0.0.0",ssl_context=('cert.pem', 'key.pem'), port=8080)
