from flask import Flask, render_template, redirect, session
from flask import url_for, flash, message_flashed, request
app = Flask(__name__)
app.config['SECRET_KEY'] = 'Hello'

@app.route('/')
def home():
    return render_template("index.html")

@app.route("/login", methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form["username"]
        session['user'] = user
        return redirect(url_for('user'))
    else:
        return render_template('login.html')

@app.route("/user")
def user():
    if 'user' in session:
        return render_template("user.html")
    else:
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    return render_template("logout.html")


if __name__ == '__main__':
    app.run(debug=True)
