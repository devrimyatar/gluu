from flask import Flask, request, redirect, url_for
from flask_login import LoginManager, UserMixin, current_user, login_required, login_user, logout_user

from authlib.client import OAuth2Session

client_id="@!5856.8A6C.09D4.C454!0001!655A.E96C!0008!7AF1.6F5E.CC4B.4036"
client_secret="dbe8e016-2609-4625-8963-3d60fed32c3e"
scope = 'openid user_name'

authorize_url = "https://c2.gluu.org/oxauth/restv1/authorize"
account_url = 'https://c2.gluu.org/oxauth/restv1/userinfo'
access_token_url = 'https://c2.gluu.org/oxauth/restv1/token'
redirect_uri='https://c3.gluu.org:5000/login'


auth_session = OAuth2Session(client_id, client_secret, scope=scope)
auth_session.verify = False


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
    uri, state = auth_session.create_authorization_url(authorize_url)
    return '<a href="{0}">Click here to login</a>'.format(uri)

@app.route('/login')
def login():
    token = auth_session.fetch_access_token(url=access_token_url, 
                authorization_response=request.url, redirect_uri=redirect_uri)
    session = OAuth2Session(client_id, client_secret, token=token, scope=scope)
    resp = auth_session.get(account_url)
    claims = resp.json()
    if claims['sub']:
        user = User(claims['user_name'])
        login_user(user)
        return redirect(url_for('welcome'))
    else:
        return "Failed to authenticate"


@app.route('/welcome')
@login_required
def welcome():
    return 'Welcome ' + current_user.username

@app.route("/logoutme")
@login_required
def logoutme():
    logout_user()
    return redirect('https://c2.gluu.org/oxauth/restv1/end_session?post_logout_redirect_uri=https%3A%2F%2Fc3.gluu.org%2Fcgi-bin%2Foxd.py%2Flogout')

@app.route("/logout")
def logout():
    return "Logged out"


if __name__ == '__main__':
    app.debug=True
    app.run(host="0.0.0.0",ssl_context=('cert.pem', 'key.pem'))
