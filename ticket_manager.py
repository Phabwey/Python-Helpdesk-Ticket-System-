import csv
import os
from ticket import Ticket

FILE_NAME = "tickets.csv"

class TicketManager:
    def __init__(self):
        if not os.path.exists(FILE_NAME):
            with open(FILE_NAME, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(
                    ["Ticket ID", "Customer Name", "Issue", "Status"]
                )

    def create_ticket(self, customer_name, issue):
        ticket_id = self.generate_ticket_id()
        ticket = Ticket(ticket_id, customer_name, issue)

        with open(FILE_NAME, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(ticket.to_list())

        print(f"Ticket {ticket_id} created successfully.")

    def view_tickets(self):
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)

    def update_status(self, ticket_id, new_status):
        rows = []

        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            rows = list(reader)

        for row in rows:
            if row and row[0] == ticket_id:
                row[3] = new_status

        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(rows)

        print("Ticket updated.")

    def generate_ticket_id(self):
        with open(FILE_NAME, "r") as file:
            count = sum(1 for _ in file)

        return f"TKT-{count:03d}"
