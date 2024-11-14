from flask import redirect, render_template, request, url_for
from config import app, test_env


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/selector", methods=["GET"])
def render_selector():
    return render_template("selector.html")
