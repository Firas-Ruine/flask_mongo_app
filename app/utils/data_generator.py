from faker import Faker
import random

faker = Faker()

def generate_synthetic_data(num_records=100):
    """
    Generate synthetic transaction data using Faker.

    :param num_records: Number of records to generate.
    :return: List of synthetic transaction records.
    """
    categories = ["Electronics", "Clothing", "Books", "Toys", "Furniture"]
    transactions = []

    for _ in range(num_records):
        transaction = {
            "invoice_id": faker.uuid4(),
            "product_name": faker.word().capitalize(),
            "category": random.choice(categories),
            "quantity": random.randint(1, 10),
            "price": round(random.uniform(10.0, 500.0), 2),
            "total": lambda t: t["quantity"] * t["price"],
            "customer_name": faker.name(),
            "customer_email": faker.email(),
            "purchase_date": faker.date_time_this_year().isoformat(),
        }
        transaction["total"] = transaction["quantity"] * transaction["price"]
        transactions.append(transaction)

    return transactions
