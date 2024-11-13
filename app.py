from flask import Flask
from flask import render_template, request
app = Flask(__name__)


@app.route("/", methods=["POST"])
def index():
    return render_template("index.html", name=request.form["name"])
