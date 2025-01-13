class Loan:
    def __init__(self, subscriber_id, document_id, due_date):
        self.subscriber_id = subscriber_id
        self.document_id = document_id
        self.loan_date = None
        self.due_date = due_date
        self.return_date = None
        self.status = "active"
