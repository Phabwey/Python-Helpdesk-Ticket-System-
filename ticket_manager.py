import csv
from datetime import datetime


class TicketManager:
    def __init__(self, filename="tickets.csv"):
        self.filename = filename

    # Create ticket
    def create_ticket(
        self,
        ticket_id,
        customer_name,
        issue,
        priority,
        category,
        technician
    ):

        now = datetime.now()

        ticket = [
            ticket_id,
            customer_name,
            issue,
            category,
            technician,
            priority,
            "Open",
            now.strftime("%Y-%m-%d"),
            now.strftime("%H:%M:%S")
        ]

        with open(self.filename, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(ticket)

        print("Ticket created successfully.")

    def view_tickets(self):
    with open(self.filename, "r", newline="") as file:
        reader = csv.reader(file)

        # Skip the header row
        next(reader)

        for row in reader:
            # Skip empty or incomplete rows
            if len(row) < 9:
                continue

      print(f"Ticket ID: {row[0]}")
      print(f"Customer: {row[1]}")
      print(f"Issue: {row[2]}")
      print(f"Category: {row[3]}")
      print(f"Technician: {row[4]}")
      print(f"Priority: {row[5]}")
      print(f"Status: {row[6]}")
      print(f"Created: {row[7]} {row[8]}")
      print("-" * 40)

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

    # Update ticket status
    def update_status(self, ticket_id, new_status):

        rows = []

        with open(self.filename, "r") as file:
            reader = csv.reader(file)

            for row in reader:

                if row[0] == str(ticket_id):
                    row[6] = new_status

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

    # Export tickets
    def export_tickets(self):

        with open(self.filename, "r") as source:
            reader = csv.reader(source)

            with open(
                "exported_tickets.csv",
                "w",
                newline=""
            ) as destination:

                writer = csv.writer(destination)

                for row in reader:
                    writer.writerow(row)

        print(
            "Tickets exported successfully to "
            "'exported_tickets.csv'."
        )

    def count_tickets(self):

    open_count = 0
    closed_count = 0

    with open(self.filename, "r") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            if len(row) < 7:
                continue

            if row[6] == "Open":
                open_count += 1
            elif row[6] == "Closed":
                closed_count += 1

    print(f"Open tickets: {open_count}")
    print(f"Closed tickets: {closed_count}")
            

           


   
        

    
        
    
        

             
        