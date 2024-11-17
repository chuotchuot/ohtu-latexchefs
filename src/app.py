from flask import redirect, render_template, request, url_for
from config import app, test_env
from repositories.reference_repository import add_reference, fetch_references


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/selector", methods=["GET"])
def render_selector():
    return render_template("selector.html")

@app.route("/redirect", methods=["POST"])
def redirect_to_reference():
    reftype = request.form["reftype"]
    return redirect(f"{reftype}")
    

@app.route("/add_book_reference", methods=["GET", "POST"])
def add_book_reference():
    if request.method == "GET":
        return render_template("new_book_reference.html")
    if request.method == "POST":
        type = "Book"
        title = request.form["title"]
        year = request.form["year"]
        publisher = request.form["publisher"]
        authors = [author.strip() for author in request.form["authors"].split(";")]

        add_reference(type, title, year, authors, publisher)
        
        return redirect("/")

@app.route("/list_of_references")
def display_list_of_references():
    references_data = fetch_references()
    return render_template("list_of_references.html", references = references_data)