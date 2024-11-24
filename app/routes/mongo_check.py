from flask import Blueprint, jsonify, render_template
from app.utils.db import get_db, reconnect_db

main = Blueprint("mongo_check", __name__)


@main.route("/mongo", methods=["GET"])
def mongo_page():
    return render_template("mongo.html")


@main.route("/api/mongo/status", methods=["GET"])
def mongo_status():
    """
    Check MongoDB connectivity status.
    """
    try:
        db = get_db()
        db.command("ping")
        return jsonify({"status": "Connected"}), 200
    except Exception as e:
        return jsonify({"status": "Disconnected", "error": str(e)}), 500

@main.route("/api/mongo/reconnect", methods=["POST"])
def mongo_reconnect():
    """
    Reconnect to MongoDB instance.
    """
    try:
        reconnect_db()
        return jsonify({"message": "Reconnected to MongoDB."}), 200
    except Exception as e:
        return jsonify({"message": "Failed to reconnect.", "error": str(e)}), 500
