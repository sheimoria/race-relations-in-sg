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

# Retrieve spreadsheet values
results = lookup()['valueRanges']


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/articles")
def articles():
    values = results[0]['values']
    return render_template("resources.html", values=values, sheet='Articles')


@app.route("/books")
def books():
    values = results[1]['values']
    return render_template("resources.html", values=values, sheet='Books')


@app.route("/videos")
def videos():
    values = results[2]['values']
    return render_template("resources.html", values=values, sheet='Videos')


@app.route("/podcasts")
def podcasts():
    values = results[3]['values']
    return render_template("resources.html", values=values, sheet='Podcasts')


@app.route("/websites")
def websites():
    values = results[4]['values']
    return render_template("resources.html", values=values, sheet='Websites')


@app.route("/social")
def social():
    values = results[5]['values']
    return render_template("resources.html", values=values, sheet='Social Media', http='http')


@app.route("/others")
def others():
    values = results[6]['values']
    return render_template("resources.html", values=values, sheet='Others')
