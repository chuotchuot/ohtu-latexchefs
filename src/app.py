from flask import Flask
from flask import render_template, request, url_for
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/selctor", methods=["GET"])
def render_selector():
    return render_template("selector.html")