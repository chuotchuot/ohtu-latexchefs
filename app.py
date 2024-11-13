from flask import Flask
from flask import render_template, request
app = Flask(__name__)


@app.route("/frontpage", methods=["POST"])
def front_page():
    return render_template("frontpage.html", name=request.form["name"])