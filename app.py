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
sheets = lookup()['valueRanges']


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/search", methods=['POST'])
def search():
    results = []
    for i in range(len(sheets)):
        for j in range(len(sheets[i]['values'])):
            for k in range(len(sheets[i]['values'][j])):
                if request.form.get('search') in sheets[i]['values'][j][k]:
                    results.append(sheets[i]['values'][j])
    return render_template("resources.html", values=results, sheet='Results', http='http')


@app.route("/articles")
def articles():
    values = sheets[0]['values']
    return render_template("resources.html", values=values, sheet='Articles', http='http')


@app.route("/books")
def books():
    values = sheets[1]['values']
    return render_template("resources.html", values=values, sheet='Books', http='http')


@app.route("/videos")
def videos():
    values = sheets[2]['values']
    return render_template("resources.html", values=values, sheet='Videos', http='http')


@app.route("/podcasts")
def podcasts():
    values = sheets[3]['values']
    return render_template("resources.html", values=values, sheet='Podcasts', http='http')


@app.route("/websites")
def websites():
    values = sheets[4]['values']
    return render_template("resources.html", values=values, sheet='Websites', http='http')


@app.route("/social")
def social():
    values = sheets[5]['values']
    return render_template("resources.html", values=values, sheet='Social Media', http='http')


@app.route("/others")
def others():
    values = sheets[6]['values']
    return render_template("resources.html", values=values, sheet='Others', http='http')
