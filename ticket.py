class Ticket:
    def __init__(self, ticket_id, customer_name, issue, status="Open"):
        self.ticket_id = ticket_id
        self.customer_name = customer_name
        self.issue = issue
        self.status = status

    def to_list(self):
        return [self.ticket_id, self.customer_name, self.issue, self.status]
