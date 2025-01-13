from flask import Blueprint, request, jsonify
from app.services.loan_service import record_loan, return_loan

main = Blueprint("loan_routes", __name__)

@main.route('/', methods=['POST'])
def record():
    data = request.json
    return jsonify(record_loan(data))

@main.route('/<loan_id>/return', methods=['PUT'])
def return_book(loan_id):
    return jsonify(return_loan(loan_id))
