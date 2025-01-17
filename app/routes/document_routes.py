from flask import Blueprint, jsonify, request
from app.services.document_service import get_all_documents, create_document, update_document, delete_document

main = Blueprint("document_routes", __name__)

@main.route("/", methods=["GET"])
def get_documents():
    search_query = request.args.get("search", "").strip()
    return jsonify(get_all_documents(search_query))

@main.route("/", methods=["POST"])
def add_document():
    data = request.json
    return jsonify(create_document(data)), 201

@main.route("/<id>", methods=["PUT"])
def edit_document(id):
    data = request.json
    return jsonify(update_document(id, data))

@main.route("/<id>", methods=["DELETE"])
def remove_document(id):
    delete_document(id)
    return jsonify({"message": "Document deleted successfully."})
