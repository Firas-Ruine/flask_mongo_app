from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, timedelta
from app.utils.db import get_db
from app.utils.email_utils import send_email  # Create this utility to send emails

def check_due_loans():
    db = get_db()
    tomorrow = datetime.now() + timedelta(days=1)
    tomorrow_start = tomorrow.replace(hour=0, minute=0, second=0, microsecond=0)
    tomorrow_end = tomorrow.replace(hour=23, minute=59, second=59, microsecond=999999)

    # Find loans due tomorrow
    due_loans = db.loans.find({"due_date": {"$gte": tomorrow_start, "$lte": tomorrow_end}})
    for loan in due_loans:
        # Get subscriber's email
        subscriber = db.subscribers.find_one({"_id": loan["subscriber_id"]})
        if subscriber and "email" in subscriber:
            send_email(
                to=subscriber["email"],
                subject="Reminder: Loan Due Tomorrow",
                body=f"Dear {subscriber['first_name']} {subscriber['last_name']},\n\n"
                     f"This is a friendly reminder that your loaned document '{loan['document_id']}' is due tomorrow.\n"
                     f"Please return it to avoid penalties.\n\nThank you!"
            )

def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(check_due_loans, "cron", hour=9)
    scheduler.start()
