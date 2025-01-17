from flask import Blueprint, render_template, flash
from app.services.category_service import get_enabled_categories, get_all_categories

main = Blueprint("html_routes", __name__)

# Dashboard
@main.route("/dashboard", methods=["GET"])
def dashboard_page():
    return render_template("dashboard.html") 

# Subscribers Pages
@main.route("/subscribers/create", methods=["GET"])
def create_subscriber_page():
    return render_template("subscribers_create.html")

@main.route("/subscribers/list", methods=["GET"])
def list_subscribers_page():
    return render_template("subscribers_list.html")

# Documents Pages
@main.route("/documents/create", methods=["GET"])
def create_document_page():
    try:
        enabled_categories = get_enabled_categories()["categories"]
    except Exception as e:
        enabled_categories = []
        flash(f"Error fetching categories: {e}", "error")
    return render_template("documents_create.html", categories=enabled_categories)

@main.route("/documents/list", methods=["GET"])
def list_documents_page():
    return render_template("documents_list.html")

# Loans Pages
@main.route("/loans/create", methods=["GET"])
def create_loan_page():
    return render_template("loans_create.html")

@main.route("/loans/list", methods=["GET"])
def list_loans_page():
    return render_template("loans_list.html")

# Categories Page
@main.route("/categories", methods=["GET"])
def categories_page():
    try:
        categories = get_all_categories()["categories"]
    except Exception as e:
        categories = []
        flash(f"Error fetching categories: {e}", "error")
    return render_template("categories.html", categories=categories)
