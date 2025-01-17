from flask import Blueprint, render_template

main = Blueprint("html_routes", __name__)

# Dashboard
@main.route("/dashboard", methods=["GET"])
def dashboard_page():
    return render_template("dashboard.html") 

# Subscribers Pages
@main.route("/subscribers/create", methods=["GET"])
def create_subscriber_page():
    return render_template("subscribers_create.html")  # Page for creating subscribers

@main.route("/subscribers/list", methods=["GET"])
def list_subscribers_page():
    return render_template("subscribers_list.html")  # Page for listing subscribers

# Documents Pages
@main.route("/documents/create", methods=["GET"])
def create_document_page():
    return render_template("documents_create.html")  # Page for creating documents

@main.route("/documents/list", methods=["GET"])
def list_documents_page():
    return render_template("documents_list.html")  # Page for listing documents

# Loans Pages
@main.route("/loans/create", methods=["GET"])
def create_loan_page():
    return render_template("loans_create.html")  # Page for creating loans

@main.route("/loans/list", methods=["GET"])
def list_loans_page():
    return render_template("loans_list.html")  # Page for listing loans

# Charts
@main.route("/charts", methods=["GET"])
def charts_page():
    return render_template("charts.html")  # Page for displaying charts
