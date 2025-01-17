from flask import Blueprint, jsonify, request
from app.services.loan_service import get_all_loans, create_loan, update_loan, delete_loan

main = Blueprint("loan_routes", __name__)

@main.route("/", methods=["GET"])
def get_loans():
    search_query = request.args.get("search", "").strip()
    return jsonify(get_all_loans(search_query))

@main.route("/", methods=["POST"])
def add_loan():
    data = request.json
    return jsonify(create_loan(data)), 201

@main.route("/<id>", methods=["PUT"])
def edit_loan(id):
    data = request.json
    return jsonify(update_loan(id, data))

@main.route("/<id>", methods=["DELETE"])
def remove_loan(id):
    delete_loan(id)
    return jsonify({"message": "Loan deleted successfully."})
