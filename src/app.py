from io import BytesIO
from flask import redirect, render_template, request, jsonify, send_file
from config import app, test_env
from entities.reference import Reference
from repositories.reference_repository import (
    save_reference, fetch_references, fetch_filtered_references,
    delete_reference,  fetch_one_reference, edit_reference,
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

@app.route("/add_reference", methods=["GET", "POST"])
def add_reference():
    if request.method == "GET":
        reference_type = request.args.get('reference_type')

        return render_template("new_reference.html", reference_type=reference_type)

    reference = Reference()

    reference.add_values_from_dictionary(request.form.items())
    reference.set_reference_key(generate_reference_key(reference))

    save_reference(reference)

    return redirect("/")

@app.route("/add_reference_with_doi", methods=["GET", "POST"])
def add_reference_with_doi():
    if request.method == "GET":
        return render_template("add_ref_with_doi.html")
    doi = request.form["doi"]
    reference = Reference()
    data = get_ref_info_with_doi(doi)

    reference.add_values_from_doi(data)
    reference.set_reference_key(generate_reference_key(reference))

    save_reference(reference)

    return redirect("/")

@app.route("/list_of_references", methods=["GET", "POST"])
def display_list_of_references():
    reference_data = fetch_references()
    if request.method == "GET" or request.form["state"] == "off" :
        return render_template("list_of_references.html", references=reference_data[0],toggle="off")
    # if request.method == "POST":
    state = request.form["state"]
    return render_template("list_of_references.html", references=reference_data[1], toggle=state)

@app.route("/filter_references", methods=['GET', 'POST'])
def filter_list_of_references():
    query = request.form["query"]
    filtered_data = fetch_filtered_references(query)
    return render_template("list_of_references.html", references=filtered_data[0],toggle="off")

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
    reference_id = request.form["id"]
    confirmed: bool = request.form["confirmed"] == "1"
    reference = fetch_one_reference(reference_id)

    if confirmed:

        reference = Reference()

        for field, value in request.form.items():
            setattr(reference, field, value)

        edit_reference(reference_id, reference)

        return redirect("/list_of_references")
    #else:

    return render_template("edit.html", reference=reference,
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
