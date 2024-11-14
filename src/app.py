from flask import redirect, render_template, request, url_for
from config import app, test_env


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/selector", methods=["GET"])
def render_selector():
    return render_template("selector.html")

@app.route("/add_book_reference", methods=["GET", "POST"])
def add_book_reference():
    if request.method == "GET":
        return render_template("new_book_reference.html")
    if request.method == "POST":
        title = request.form["title"]
        year = request.form["year"]
        publisher = request.form["publisher"]
        authors = [author.strip() for author in request.form["authors"].split(";")]
        return redirect("/")