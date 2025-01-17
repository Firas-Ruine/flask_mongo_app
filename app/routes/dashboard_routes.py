from flask import Blueprint, jsonify
from app.services.dashboard_service import (
    get_subscriber_growth,
    get_active_loans,
    get_document_distribution,
)
main = Blueprint("dashboard_routes", __name__)

@main.route("/subscriber-growth", methods=["GET"])
def subscriber_growth():
    return jsonify(get_subscriber_growth())

@main.route("/active-loans", methods=["GET"])
def active_loans():
    return jsonify(get_active_loans())

@main.route("/document-distribution", methods=["GET"])
def document_distribution():
    return jsonify(get_document_distribution())
