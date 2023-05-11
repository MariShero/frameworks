from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    lst = ["hello world!", "python programming", "backend"]
    return render_template("index.html", lst=lst)


@app.route('/<name>/<age>')
def user(name, age):
    return render_template("user.html", user_name=name, user_age=age)


if __name__ == '__main__':
    app.run(debug=True)