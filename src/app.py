from io import BytesIO
from flask import redirect, render_template, request, jsonify, send_file
from config import app, test_env
from entities.reference import Reference
from repositories.reference_repository import (
    add_reference, fetch_references, delete_reference,
    fetch_one_reference, edit_reference, create_input_dictionary,
    fetch_reference_keys, create_bibtex_string, create_readable_string,
    get_ref_info_with_doi, generate_reference_key
    )
from db_helper import reset_db

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/selector", methods=["GET"])
def render_selector():
    return render_template("selector.html")

@app.route("/add_reference", methods=["POST"])
def add_any_reference():
    reference = Reference()

    for key, value in request.form.items():
        setattr(reference, key, value)

    reference.reference_key = generate_reference_key(reference)

    add_reference(reference)

    return redirect("/")

@app.route("/add_book_reference")
def add_book_reference():
    return render_template("new_book_reference.html", ref_keys=fetch_reference_keys())

@app.route("/add_inbook_reference", methods=["GET", "POST"])
def add_inbook_reference():
    return render_template("new_inbook_reference.html", ref_keys=fetch_reference_keys())

@app.route("/add_article_reference", methods=["GET", "POST"])
def add_article_reference():
    return render_template("new_article_reference.html", ref_keys=fetch_reference_keys())

@app.route("/add_misc_reference", methods=["GET", "POST"])
def add_misc_reference():
    return render_template("new_misc_reference.html", ref_keys=fetch_reference_keys())

@app.route("/add_reference_with_doi", methods=["GET", "POST"])
def add_reference_with_doi():
    if request.method == "GET":
        return render_template("add_ref_with_doi.html")
    doi = request.form["doi"]
    ref_info = get_ref_info_with_doi(doi)

    authors_str = [author.strip() for author in ref_info.get("author").split("and")]

    inputs = create_input_dictionary()
    inputs["ref_type"] = "article"
    inputs["title"] = ref_info.get("title")
    inputs["authors"] = authors_str
    inputs["year"] = ref_info.get("year")
    inputs["journal"] = ref_info.get("journal")
    inputs["volume"] = ref_info.get("volume")
    inputs["number"] = ref_info.get("number")
    inputs["page"] = ref_info.get("page")
    inputs["month"] = ref_info.get("month")
    inputs["note"] = ref_info.get("note")

    inputs["ref_key"] = "temp"

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
    reference = fetch_one_reference(ref_id)
    readable_string = {"id":reference.id,"text":create_readable_string(reference)}
    return render_template("delete.html", reference=readable_string)

@app.route("/edit", methods=["POST"])
def edit():
    ref_id = request.form["id"]
    confirmed: bool = request.form["confirmed"] == "1"
    reference = fetch_one_reference(ref_id)
    if confirmed:
        reference_type = reference.reference_type
        inputs = create_input_dictionary()

        inputs["reference_type"]= reference.reference_type

        if reference_type == "book":
            inputs["year"] = request.form["year"]
            inputs["publisher"] = request.form["publisher"]
            inputs["editors"] = [editor.strip() for editor in request.form["editors"].split(";")]
            inputs["authors"] = [author.strip() for author in request.form["authors"].split(";")]

        elif reference_type == "inbook":
            inputs["booktitle"] = request.form["booktitle"]
            inputs["year"] = request.form["year"]
            inputs["publisher"] = request.form["publisher"]
            inputs["editors"] = [editor.strip() for editor in request.form["editors"].split(";")]
            inputs["authors"] = [author.strip() for author in request.form["authors"].split(";")]

        elif reference_type == "misc":
            inputs["authors"] = [author.strip() for author in request.form["authors"].split(";")]
            inputs["howpublished"] = request.form["howpublished"]
            inputs["month"] = request.form["month"]
            inputs["year"] = request.form["year"]
            inputs["note"] = request.form["note"]

        elif reference_type == "article":
            inputs["authors"] = [author.strip() for author in request.form["authors"].split(";")]
            inputs["journal"] = request.form["journal"]
            inputs["year"] = request.form["year"]
            inputs["volume"] = request.form["volume"]
            inputs["number"] = request.form["number"]
            inputs["page"] = request.form["pages"]
            inputs["month"] = request.form["month"]
            inputs["note"] = request.form["note"]

        elif reference_type == "misc":
            inputs["reference_type"] ="misc"
            inputs["authors"] = [author.strip() for author in request.form["authors"].split(";")]
            inputs["howpublished"] = request.form["howpublished"]
            inputs["month"] = request.form["month"]
            inputs["year"] = request.form["year"]
            inputs["note"] = request.form["note"]
            inputs["reference_key"] = request.form["reference_key"]
            inputs["keywords"] = [keyword.strip() for
                                  keyword in request.form["keywords"].split(";")]

        inputs["title"] = request.form["title"]
        inputs["reference_key"] = request.form["reference_key"]
        inputs["keywords"] = [keyword.strip() for
                                keyword in request.form["keywords"].split(";")]

        edit_reference(ref_id, inputs)
        return redirect("/list_of_references")
    #else:
    reference = fetch_one_reference(ref_id)
    authors: str = ";".join(reference.authors.split(" and "))
    editors: str = ";".join(reference.editors.split(" and "))
    return render_template("edit.html", reference=reference, authors=authors, editors=editors,
                           ref_keys=fetch_reference_keys())

@app.route("/download/<int:ref_id>.bib", methods=["GET"])
def download_reference(ref_id: int):
    reference = fetch_one_reference(ref_id)
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
