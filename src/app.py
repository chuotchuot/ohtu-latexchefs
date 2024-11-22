from flask import redirect, render_template, request, jsonify
from config import app, test_env
from repositories.reference_repository import add_reference, fetch_references
from db_helper import reset_db

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/selector", methods=["GET", "POST"])
def render_selector():
    if request.method == "GET":
        return render_template("selector.html")
    if request.method == "POST":
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
        reference_key = request.form["reference_key"]
        keywords = request.form["keywords"]

        add_reference(type, title, year, authors, publisher, reference_key, keywords)
        
        return redirect("/")

@app.route("/list_of_references", methods=["GET", "POST"])
def display_list_of_references():
    references_data = fetch_references()
    if request.method == "GET":
        return render_template("list_of_references.html", references=references_data, toggle="off")
    if request.method == "POST":
        state = request.form["state"]
        return render_template("list_of_references.html", references=references_data, toggle=state)

if test_env:
    @app.route("/reset_db")
    def reset_database():
        reset_db()
        return jsonify({ 'message': "db reset" })