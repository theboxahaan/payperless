from flask import Flask, render_template, request, redirect, url_for



app = Flask(__name__)

@app.route('/')
def serve_login_page():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        user, pwd = request.form['username'], request.form['password']
        return redirect(url_for('dashboard'))

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


if __name__ == '__main__':
    app.run(debug='True')
