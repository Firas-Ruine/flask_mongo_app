from flask import Blueprint, request, jsonify
from app.services.category_service import (
    create_category,
    get_all_categories,
    get_enabled_categories,
    update_category,
    delete_category,
)

main = Blueprint("category_routes", __name__)

@main.route("/", methods=["POST"])
def create():
    data = request.json
    return jsonify(create_category(data))

@main.route("/", methods=["GET"])
def get_all():
    return jsonify(get_all_categories())

@main.route("/enabled", methods=["GET"])
def get_enabled():
    return jsonify(get_enabled_categories())

@main.route("/<id>", methods=["PUT"])
def update(id):
    data = request.json
    return jsonify(update_category(id, data))

@main.route("/<id>", methods=["DELETE"])
def delete(id):
    return jsonify(delete_category(id))
