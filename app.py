import os

from flask import Flask, flash, jsonify, redirect, render_template, request
from tempfile import mkdtemp
from helper import lookup

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

# Index
@app.route("/")
def index(): 
    return render_template("index.html")

@app.route("/articles")
def articles():
    values = lookup('Articles')
    return render_template("resources.html", values=reversed(values))

@app.route("/books")
def books():
    values = lookup('Books')
    return render_template("resources.html", values=reversed(values))

@app.route("/videos")
def videos():
    values = lookup('Videos')
    return render_template("resources.html", values=reversed(values))

@app.route("/podcasts")
def podcasts():
    values = lookup('Podcasts')
    return render_template("resources.html", values=reversed(values))

@app.route("/websites")
def websites():
    values = lookup('Websites')
    return render_template("resources.html", values=reversed(values))

@app.route("/social")
def social():
    values = lookup('Social Media')
    return render_template("resources.html", values=reversed(values))

@app.route("/others")
def others():
    values = lookup('Others')
    return render_template("resources.html", values=values)