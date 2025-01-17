from app.utils.db import get_db
from datetime import datetime

def get_subscriber_growth():
    db = get_db()
    pipeline = [
        {"$addFields": {"month": {"$month": "$date_of_registration"}}},
        {
            "$group": {
                "_id": "$month",
                "count": {"$sum": 1}
            }
        },
        {"$sort": {"_id": 1}}
    ]
    growth = list(db.subscribers.aggregate(pipeline))
    months = [str(item["_id"]) for item in growth]
    counts = [item["count"] for item in growth]
    return {"months": months, "counts": counts}

def get_active_loans():
    db = get_db()
    pipeline = [
        {"$match": {"status": "active"}},
        {"$addFields": {"month": {"$month": "$loan_date"}}},
        {
            "$group": {
                "_id": "$month",
                "count": {"$sum": 1}
            }
        },
        {"$sort": {"_id": 1}}
    ]
    active = list(db.loans.aggregate(pipeline))
    months = [str(item["_id"]) for item in active]
    counts = [item["count"] for item in active]
    return {"months": months, "counts": counts}

def get_document_distribution():
    db = get_db()
    pipeline = [
        {
            "$group": {
                "_id": "$category",
                "count": {"$sum": 1}
            }
        }
    ]
    distribution = list(db.documents.aggregate(pipeline))
    categories = [item["_id"] for item in distribution]
    counts = [item["count"] for item in distribution]
    return {"categories": categories, "counts": counts}
