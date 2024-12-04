from io import BytesIO
from flask import redirect, render_template, request, jsonify, send_file
from config import app, test_env
from repositories.reference_repository import (
    add_reference, fetch_references, delete_reference,
    fetch_reference, edit_reference, create_input_dictionary,
    fetch_reference_keys, create_bibtex_string
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
        return render_template("new_book_reference.html", ref_keys=fetch_reference_keys())
    # if request.method == "POST":
    inputs = create_input_dictionary()
    inputs["ref_type"] = "book"
    inputs["title"] = request.form["title"]
    inputs["year"] = request.form["year"]
    inputs["publisher"] = request.form["publisher"]
    inputs["editors"] = [editor.strip() for editor in request.form["editor"].split(";")]
    inputs["authors"] = [author.strip() for author in request.form["authors"].split(";")]
    inputs["ref_key"] = request.form["reference_key"]
    inputs["keywords"] = [keyword.strip() for keyword in request.form["keywords"].split(";")]

    add_reference(inputs)

    return redirect("/")

@app.route("/add_inbook_reference", methods=["GET", "POST"])
def add_inbook_reference():
    if request.method == "GET":
        return render_template("new_inbook_reference.html", ref_keys=fetch_reference_keys())
    # if request.method == "POST":
    inputs = create_input_dictionary()
    inputs["ref_type"] = "inbook"
    inputs["title"] = request.form["title"]
    inputs["booktitle"] = request.form["booktitle"]
    inputs["year"] = request.form["year"]
    inputs["publisher"] = request.form["publisher"]
    inputs["editors"] = [editor.strip() for editor in request.form["editors"].split(";")]
    inputs["authors"] = [author.strip() for author in request.form["authors"].split(";")]
    inputs["ref_key"] = request.form["reference_key"]
    inputs["keywords"] = [keyword.strip() for keyword in request.form["keywords"].split(";")]

    add_reference(inputs)

    return redirect("/")

@app.route("/add_article_reference", methods=["GET", "POST"])
def add_article_reference():
    if request.method == "GET":
        return render_template("new_article_reference.html", ref_keys=fetch_reference_keys())
    # if request.method == "POST":
    inputs = create_input_dictionary()
    inputs["ref_type"] = "article"
    inputs["title"] = request.form["title"]
    inputs["authors"] = [author.strip() for author in request.form["authors"].split(";")]
    inputs["journal"] = request.form["journal"]
    inputs["year"] = request.form["year"]
    inputs["volume"] = request.form["volume"]
    inputs["number"] = request.form["number"]
    inputs["page"] = request.form["pages"]
    inputs["month"] = request.form["month"]
    inputs["note"] = request.form["note"]

    inputs["ref_key"] = request.form["reference_key"]
    inputs["keywords"] = [keyword.strip() for keyword in request.form["keywords"].split(";")]

    add_reference(inputs)

    return redirect("/")

@app.route("/add_misc_reference", methods=["GET", "POST"])
def add_misc_reference():
    if request.method == "GET":
        return render_template("new_misc_reference.html", ref_keys=fetch_reference_keys())
    # if request.method == "POST":
    inputs = create_input_dictionary()
    inputs["ref_type"] = "misc"
    inputs["authors"] = [author.strip() for author in request.form["authors"].split(";")]
    inputs["title"] = request.form["title"]
    inputs["howpublished"] = request.form["howpublished"]
    inputs["month"] = request.form["month"]
    inputs["year"] = request.form["year"]
    inputs["note"] = request.form["note"]
    inputs["ref_key"] = request.form["reference_key"]
    inputs["keywords"] = [keyword.strip() for keyword in request.form["keywords"].split(";")]

    add_reference(inputs)

    return redirect("/")

@app.route("/list_of_references", methods=["GET", "POST"])
def display_list_of_references():
    reference_data = fetch_references()
    if request.method == "GET" or request.form["state"] == "off" :
        return render_template("list_of_references.html", references=reference_data[0],toggle="off")
    # if request.method == "POST":
    state = request.form["state"]
    return render_template("list_of_references.html", references=reference_data[1], toggle=state)


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
    reference = fetch_reference(ref_id)
    if confirmed:
        ref_type = reference.reference_type
        inputs = create_input_dictionary()

        if ref_type == "book":
            inputs["ref_type"] = "book"
            inputs["title"] = request.form["title"]
            inputs["year"] = request.form["year"]
            inputs["publisher"] = request.form["publisher"]
            inputs["editors"] = [editor.strip() for editor in request.form["editor"].split(";")]
            inputs["authors"] = [author.strip() for author in request.form["authors"].split(";")]

        elif ref_type == "inbook":
            inputs["ref_type"] = "inbook"
            inputs["title"] = request.form["title"]
            inputs["booktitle"] = request.form["booktitle"]
            inputs["year"] = request.form["year"]
            inputs["publisher"] = request.form["publisher"]
            inputs["editors"] = [editor.strip() for editor in request.form["editors"].split(";")]
            inputs["authors"] = [author.strip() for author in request.form["authors"].split(";")]

        elif ref_type == "misc":
            inputs["ref_type"] = "misc"
            inputs["authors"] = [author.strip() for author in request.form["authors"].split(";")]
            inputs["title"] = request.form["title"]
            inputs["howpublished"] = request.form["howpublished"]
            inputs["month"] = request.form["month"]
            inputs["year"] = request.form["year"]
            inputs["note"] = request.form["note"]

        elif ref_type == "article":
            inputs["ref_type"] = "article"
            inputs["title"] = request.form["title"]
            inputs["authors"] = [author.strip() for author in request.form["authors"].split(";")]
            inputs["journal"] = request.form["journal"]
            inputs["year"] = request.form["year"]
            inputs["volume"] = request.form["volume"]
            inputs["number"] = request.form["number"]
            inputs["page"] = request.form["pages"]
            inputs["month"] = request.form["month"]
            inputs["note"] = request.form["note"]

        inputs["ref_key"] = request.form["reference_key"]
        inputs["keywords"] = [keyword.strip() for
                                keyword in request.form["keywords"].split(";")]


        elif ref_type == "miscellaneous":
            inputs["ref_type"] ="miscellaneous"
            inputs["authors"] = [author.strip() for author in request.form["authors"].split(";")]
            inputs["title"] = request.form["title"]
            inputs["howpublished"] = request.form["howpublished"]
            inputs["month"] = request.form["month"]
            inputs["year"] = request.form["year"]
            inputs["note"] = request.form["note"]
            inputs["ref_key"] = request.form["reference_key"]
            inputs["keywords"] = [keyword.strip() for
                                  keyword in request.form["keywords"].split(";")]

        edit_reference(ref_id, inputs)
        return redirect("/list_of_references")
    #else:
    reference = fetch_reference(ref_id)
    authors: str = ";".join(reference.author.split(" and "))
    editors: str = ";".join(reference.editor.split(" and "))
    return render_template("edit.html", reference=reference, authors=authors, editors=editors,
                           ref_keys=fetch_reference_keys())

@app.route("/download/<int:ref_id>.bib", methods=["GET"])
def download_reference(ref_id: int):
    reference = fetch_reference(ref_id)
    if reference is None:
        redirect("/")
    bibtex: str = create_bibtex_string(reference)
    return send_file(BytesIO(bibtex.encode()), download_name=f"{reference.reference_key}.bib")

@app.route("/download/allreferences.bib", methods=["GET"])
def download_references():
    references = fetch_references()
    bibtex: str = ""
    for reference in references[1]:
        bibtex += f"{reference['text']}\n"
    return send_file(BytesIO(bibtex.encode()), download_name="allreferences.bib")

if test_env:
    @app.route("/reset_db")
    def reset_database():
        reset_db()
        return jsonify({ 'message': "db reset" })
