from flask import redirect, render_template, request, jsonify
from config import app, test_env, toggle
from repositories.reference_repository import add_reference, fetch_references
from db_helper import reset_db

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
        #reference_key = request.form["reference_key"]
        #keywords = request.form["keywords"]

        add_reference(type, title, year, authors, publisher, reference_key="Testi", keywords="Keyword 1, Keyword 2")
        
        return redirect("/")

@app.route("/list_of_references")
def display_list_of_references():
    # Add if statement here to determine how reference data is fetched
    references_data = fetch_references()
    return render_template("list_of_references.html", references=references_data, view=toggle.get_state())

@app.route("/toggle_list", methods=["POST"])
def toggle_list():
    toggle.change_state()
    return redirect("/list_of_references")

if test_env:
    @app.route("/reset_db")
    def reset_database():
        reset_db()
        return jsonify({ 'message': "db reset" })