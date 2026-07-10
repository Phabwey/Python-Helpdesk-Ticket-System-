from ticket_manager import TicketManager

manager = TicketManager()

while True:
    print("\n=== IT Help Desk Ticket System ===")
    print("1. Create ticket")
    print("2. View tickets")
    print("3. Update ticket status")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Customer name: ")
        issue = input("Issue description: ")
        manager.create_ticket(name, issue)

    elif choice == "2":
        manager.view_tickets()

    elif choice == "3":
        ticket_id = input("Ticket ID: ")
        status = input("New status (Open/In Progress/Resolved): ")
        manager.update_status(ticket_id, status)

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")
