import csv
from datetime import datetime


class TicketManager:
    def __init__(self, filename="tickets.csv"):
        self.filename = filename

    # Create ticket with priority and date/time
    def create_ticket(self, ticket_id, customer_name, issue, priority):
        now = datetime.now()

        ticket = [
            ticket_id,
            customer_name,
            issue,
            priority,
            "Open",
            now.strftime("%Y-%m-%d"),
            now.strftime("%H:%M:%S")
        ]

        with open(self.filename, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(ticket)

        print("Ticket created successfully.")

    # View all tickets
    def view_tickets(self):
        with open(self.filename, "r") as file:
            reader = csv.reader(file)

            for row in reader:
                print(row)

    # Search ticket by ID
    def search_ticket(self, ticket_id):
        with open(self.filename, "r") as file:
            reader = csv.reader(file)

            for row in reader:
                if row[0] == str(ticket_id):
                    print("Ticket found:")
                    print(row)
                    return

        print("Ticket not found.")

    # Update status
    def update_status(self, ticket_id, new_status):
        rows = []

        with open(self.filename, "r") as file:
            reader = csv.reader(file)

            for row in reader:
                if row[0] == str(ticket_id):
                    row[4] = new_status

                rows.append(row)

        with open(self.filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(rows)

        print("Ticket updated.")

    # Delete ticket
    def delete_ticket(self, ticket_id):
        rows = []

        with open(self.filename, "r") as file:
            reader = csv.reader(file)

            for row in reader:
                if row[0] != str(ticket_id):
                    rows.append(row)

        with open(self.filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(rows)

        print("Ticket deleted.")
