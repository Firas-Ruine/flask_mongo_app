from app.utils.db import get_db
from datetime import datetime

def record_loan(data):
    db = get_db()
    loan_id = db.loans.insert_one(data).inserted_id
    db.documents.update_one({"_id": data["document_id"]}, {"$inc": {"available_copies": -1}})
    return {"message": "Loan recorded", "id": str(loan_id)}

def return_loan(loan_id):
    db = get_db()
    db.loans.update_one({"_id": loan_id}, {"$set": {"return_date": datetime.now(), "status": "returned"}})
    return {"message": "Loan returned"}
