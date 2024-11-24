from flask import Blueprint, jsonify, render_template
from app.utils.db import get_db

# Define the Blueprint
main = Blueprint("healthcheck", __name__)

@main.route("/", methods=["GET"])
def health_check():
    return render_template("index.html")

@main.route("/mongo", methods=["GET"])
def mongo_health_check():
    try:
        db = get_db()
        # Check MongoDB connectivity by running a simple query
        db.command("ping")
        return jsonify({"status": "OK", "mongo": "Connected"})
    except Exception as e:
        return jsonify({"status": "ERROR", "mongo": str(e)}), 500
