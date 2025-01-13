from flask import Blueprint, request, jsonify
from app.services.document_service import create_document, get_all_documents

main = Blueprint("document_routes", __name__)

@main.route('/', methods=['POST'])
def create():
    data = request.json
    return jsonify(create_document(data))

@main.route('/', methods=['GET'])
def get_all():
    return jsonify(get_all_documents())
