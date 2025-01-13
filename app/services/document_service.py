from app.utils.db import get_db

def create_document(data):
    db = get_db()
    document_id = db.documents.insert_one(data).inserted_id
    return {"message": "Document created", "id": str(document_id)}

def get_all_documents():
    db = get_db()
    documents = list(db.documents.find())
    for doc in documents:
        doc['_id'] = str(doc['_id'])
    return {"documents": documents}
