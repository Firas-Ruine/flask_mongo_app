from flask import Blueprint, jsonify, request
from app.utils.db import get_db
from app.services.data_service import generate_and_insert_data

main = Blueprint("data_routes", __name__)

@main.route("/test", methods=["GET"])
def test_data_route():
    return jsonify({"message": "Data routes working!"})

@main.route("/generate", methods=["POST"])
def generate_data():
    num_records = request.json.get("num_records", 100)
    records_inserted = generate_and_insert_data(num_records)
    return jsonify({"message": f"{records_inserted} records generated and inserted into MongoDB."})

@main.route("/list", methods=["GET"])
def list_data():
    """
    Fetch data with optional search and sorting.
    Query Parameters:
      - search: Keyword to search in product_name.
      - sort_by: Field to sort by (e.g., 'price', 'purchase_date').
      - order: Sort order ('asc' or 'desc'). Default is 'asc'.
      - limit: Number of records to return. Default is 10.
    """
    db = get_db()
    collection = db["transactions"]

    # Get query parameters
    search = request.args.get("search", "").strip()
    sort_by = request.args.get("sort_by", "purchase_date")  # Default sort field
    order = request.args.get("order", "asc")
    limit = int(request.args.get("limit", 10))

    # Build query
    query = {}
    if search:
        query["product_name"] = {"$regex": search, "$options": "i"}  # Case-insensitive search

    # Build sort order
    sort_order = 1 if order == "asc" else -1

    # Fetch data with search, sort, and limit
    data = list(
        collection.find(query).sort(sort_by, sort_order).limit(limit)
    )

    # Convert ObjectId to string for JSON serialization
    for record in data:
        record["_id"] = str(record["_id"])

    return jsonify(data)
