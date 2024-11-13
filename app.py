from flask import Flask
from flask import render_template, request
app = Flask(__name__)


@app.route("/frontpage", methods=["POST"])
def index():
    return render_template("frontpage.html", name=request.form["name"])
