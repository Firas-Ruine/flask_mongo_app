from flask import Blueprint, render_template, jsonify, request
from app.utils.db import get_db
from app.services.data_service import generate_and_insert_data

main = Blueprint("data_routes", __name__)

@main.route("/generate", methods=["GET"])
def generate_page():
    return render_template("generate.html")

@main.route("/list", methods=["GET"])
def list_page():
    return render_template("list.html")

@main.route("/api/data/generate", methods=["POST"])
def generate_data():
    num_records = request.json.get("num_records", 100)
    records_inserted = generate_and_insert_data(num_records)
    return jsonify({"message": f"{records_inserted} records generated and inserted into MongoDB."})

@main.route("/api/data/list", methods=["GET"])
def list_data():
    """
    Fetch paginated data with optional search and sorting.
    Query Parameters:
      - search: Keyword to search in product_name.
      - sort_by: Field to sort by (e.g., 'price', 'purchase_date').
      - order: Sort order ('asc' or 'desc'). Default is 'asc'.
      - page: Page number for pagination. Default is 1.
      - limit: Number of records per page. Default is 10.
    """
    db = get_db()
    collection = db["transactions"]

    search = request.args.get("search", "").strip()
    sort_by = request.args.get("sort_by", "purchase_date") 
    order = request.args.get("order", "asc")
    page = int(request.args.get("page", 1)) 
    limit = int(request.args.get("limit", 10))

    # Build query
    query = {}
    if search:
        query["product_name"] = {"$regex": search, "$options": "i"} 

    sort_order = 1 if order == "asc" else -1

    skip = (page - 1) * limit

    data = list(
        collection.find(query).sort(sort_by, sort_order).skip(skip).limit(limit)
    )

    total_count = collection.count_documents(query)

    for record in data:
        record["_id"] = str(record["_id"])

    return jsonify({
        "data": data,
        "page": page,
        "limit": limit,
        "total_count": total_count,
        "total_pages": (total_count + limit - 1) // limit, 
    })
