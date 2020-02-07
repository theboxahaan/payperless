from flask import Flask, render_template, request, redirect, url_for, session
from flask_login import LoginManager, login_user, login_required, current_user, logout_user
from User import User
from pipeline import Pipeline, parse_pipeline
from  userfiles_utils import upload2bucket
import uuid

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
            return redirect(url_for('filestack'))
        else:
            return redirect(url_for('serve_login_page'))

@app.route('/dashboard')
@login_required
def filestack():
    return render_template('dashboard.html', cur_name = current_user._id)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('serve_login_page'))


@login_required
@app.route('/workflow')
def workflow():
    return render_template('workflow.html', cur_name = current_user._id)


@login_required
@app.route('/workflow/create', methods=['POST'])
def workflow_create():
    if request.method == 'POST':
        r_pipeline = request.form['pipeline']
        f = request.files['pdf']
        p_pipeline = parse_pipeline(r_pipeline)
        
        # Commit Pipeline to DB

        filename = str(uuid.uuid4()) + '.pdf'
        bucketname = current_user._userdir
        f.save('./tempfile')
        upload2bucket('./tempfile', bucketname, filename)

        temp = Pipeline(filename, current_user._id, p_pipeline, 1, "application", "None")
        temp.commit(current_user._userdir)
        return "Workflow Created"       




@login_manager.user_loader
def load_user(userid):
    return User(userid)

if __name__ == '__main__':
    app.run(debug='True')
