from datetime import datetime

class Subscriber:
    def __init__(self, first_name, last_name, email, phone, address):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.address = address
        self.date_of_registration = datetime.now()
        self.current_loans = []
        self.loan_history = []
