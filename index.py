from flask import Flask, render_template, request, redirect, url_for, session
from flask_login import LoginManager, login_user, login_required, current_user
from User import User

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def serve_login_page():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        user, pwd = request.form['username'], request.form['password']
        user = User(user)
        if user.authenticate(pwd):
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            return redirect(url_for('serve_login_page'))

@app.route('/dashboard')
@login_required
def dashboard():

    return render_template('dashboard.html', cur_name = current_user._id)



@login_manager.user_loader
def load_user(userid):
    return User(userid)

if __name__ == '__main__':
    app.run(debug='True')
