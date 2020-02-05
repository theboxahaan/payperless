from flask import Flask, render_template, request



app = Flask(__name__)

@app.route('/')
def serve_login_page():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        user, pwd = request.form['username'], request.form['password']
        return user+' '+pwd

if __name__ == '__main__':
    app.run(debug='True')
