from flask import render_template
from app import app

@app.route("/")
@app.route("/index")
def index():
    user = {"username": "Phillip"}
    posts = [
        {
            "author":{"username" : "Bob"},
            "body" : "Wellington is beautiful today!"
        },
        {
            "author":{"username" : "Jane"},
            "body" : "It's not even summer and I have a tan line!"
        }
    ]
    return render_template("index.html", title="Home", user=user, posts=posts)