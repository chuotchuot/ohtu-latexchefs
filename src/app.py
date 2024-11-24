from flask import redirect, render_template, request, jsonify
from config import app, test_env
from repositories.reference_repository import (
    add_reference, fetch_references, delete_reference,
    fetch_reference, edit_reference
    )
from db_helper import reset_db

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/selector", methods=["GET", "POST"])
def render_selector():
    if request.method == "GET":
        return render_template("selector.html")
    #if request.method == "POST":
    reftype = request.form["reftype"]
    return redirect(f"{reftype}")

@app.route("/add_book_reference", methods=["GET", "POST"])
def add_book_reference():
    if request.method == "GET":
        return render_template("new_book_reference.html")
    # if request.method == "POST":
    ref_type = "Book"
    title = request.form["title"]
    year = request.form["year"]
    publisher = request.form["publisher"]
    authors = [author.strip() for author in request.form["authors"].split(";")]
    reference_key = request.form["reference_key"]
    keywords = request.form["keywords"]

    add_reference(ref_type, title, year, authors, publisher, reference_key, keywords)

    return redirect("/")

@app.route("/list_of_references", methods=["GET", "POST"])
def display_list_of_references():
    references_data = fetch_references()
    if request.method == "GET":
        return render_template("list_of_references.html", references=references_data, toggle="off")
    # if request.method == "POST":
    state = request.form["state"]
    return render_template("list_of_references.html", references=references_data, toggle=state)


@app.route("/delete", methods=["POST"])
def delete():
    ref_id = request.form["id"]
    confirmed: bool = request.form["confirmed"] == "1"
    if confirmed:
        delete_reference(ref_id)
        return redirect("/list_of_references")
    #else:
    reference = fetch_reference(ref_id)
    return render_template("delete.html", reference=reference)

@app.route("/edit", methods=["POST"])
def edit():
    ref_id = request.form["id"]
    confirmed: bool = request.form["confirmed"] == "1"
    if confirmed:
        title = request.form["title"]
        year = request.form["year"]
        publisher = request.form["publisher"]
        authors = [author.strip() for author in request.form["authors"].split(";")]
        reference_key = request.form["reference_key"]
        keywords = request.form["keywords"]

        edit_reference(ref_id, title, year, authors, publisher, reference_key, keywords)
        return redirect("/list_of_references")
    #else:
    reference = fetch_reference(ref_id)
    authors: str = ";".join(reference.author.split(", "))
    return render_template("edit.html", reference=reference, authors=authors)

if test_env:
    @app.route("/reset_db")
    def reset_database():
        reset_db()
        return jsonify({ 'message': "db reset" })
