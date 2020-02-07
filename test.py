from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_login import LoginManager, UserMixin, login_user, login_required, current_user
from auth import auth_status, get_user

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

login_manager = LoginManager()
login_manager.init_app(app)

class User(UserMixin):

    def __init__(self, identifier):
        self._isauthenticated = False
        self._id, self._pwd, self._userdir = get_user(identifier) 

    def is_authenticated(self):
        return self._isauthenticated
    
    def is_active():
        return True
    
    def is_anonymous():
        return False

    def get_id(self):
        return self._id

    def authenticate(self, pwd):
        self._isauthenticated = pwd == self._pwd
        return self._isauthenticated


@app.route('/root')
@login_required
def root():
    return render_template('dashboard.html')


@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        user, pwd = request.form['username'], request.form['password']
        user = User(user)
        if user.authenticate(pwd):
            login_user(user)
            return redirect(url_for('root'))
        else:
            return render_template('index.html')


    else:
        return render_template('index.html')

@login_manager.user_loader
def load_user(userid):
    return User(userid)

if __name__ == '__main__':
    app.run(debug = True)
    
