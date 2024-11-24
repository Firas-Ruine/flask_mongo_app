from app.utils.db import get_db
from app.utils.data_generator import generate_synthetic_data

def generate_and_insert_data(num_records=100):
    """
    Generate synthetic data and insert it into MongoDB.

    :param num_records: Number of records to generate.
    """
    db = get_db()
    data = generate_synthetic_data(num_records)
    db["transactions"].insert_many(data)
    return len(data)
