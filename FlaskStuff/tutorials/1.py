from flask import Flask, redirect, url_for


app = Flask(__name__)


@app.route("/")
def home():

    return "<h1>Hello, World!</h1>"


@app.route("/<name>")
def user(name: str):

    return f"<h1>Hello {name}</h1>"


@app.route("/admin")
def admin():
    # Redirect user to home page
    # if attempt to access admin page
    # is made
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run()
