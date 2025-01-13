from flask import Blueprint, request, jsonify
from bson import ObjectId
from app.services.subscriber_service import (
    create_subscriber,
    get_all_subscribers,
    update_subscriber,
    delete_subscriber,
)

main = Blueprint("subscriber_routes", __name__)

@main.route("/", methods=["POST"])
def create():
    data = request.json
    return jsonify(create_subscriber(data))

@main.route("/", methods=["GET"])
def get_all():
    # Get the optional search query parameter
    search_query = request.args.get("search", "").strip()
    return jsonify(get_all_subscribers(search_query))


@main.route("/<subscriber_id>", methods=["PUT"])
def update(subscriber_id):
    if not ObjectId.is_valid(subscriber_id):
        return jsonify({"error": "Invalid subscriber ID"}), 400
    data = request.json
    result = update_subscriber(subscriber_id, data)
    if result["modified_count"] == 0:
        return jsonify({"error": "Subscriber not found or no changes made"}), 404
    return jsonify(result)

@main.route("/<subscriber_id>", methods=["DELETE"])
def delete(subscriber_id):
    if not ObjectId.is_valid(subscriber_id):
        return jsonify({"error": "Invalid subscriber ID"}), 400
    result = delete_subscriber(subscriber_id)
    if result["deleted_count"] == 0:
        return jsonify({"error": "Subscriber not found"}), 404
    return jsonify(result)
