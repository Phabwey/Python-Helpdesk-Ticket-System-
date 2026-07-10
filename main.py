while True:
    print("\n--- Helpdesk Ticket System ---")
    print("1. Create Ticket")
    print("2. View Tickets")
    print("3. Search Ticket")
    print("4. Update Status")
    print("5. Delete Ticket")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1":

        try:
            ticket_id = int(input("Ticket ID: "))
        except ValueError:
            print("Please enter a valid ticket number.")
            continue

        customer_name = input("Customer name: ")
        issue = input("Issue: ")

        priority = input(
            "Priority (Low, Medium, High): "
        ).capitalize()

        if priority not in ["Low", "Medium", "High"]:
            print("Invalid priority.")
            continue

        manager.create_ticket(
            ticket_id,
            customer_name,
            issue,
            priority
        )

    elif choice == "2":
        manager.view_tickets()

    elif choice == "3":
        ticket_id = input("Enter ticket ID: ")
        manager.search_ticket(ticket_id)

    elif choice == "4":

        ticket_id = input("Ticket ID: ")

        status = input(
            "New status (Open, In Progress, Closed): "
        ).title()

        if status not in ["Open", "In Progress", "Closed"]:
            print("Invalid status.")
            continue

        manager.update_status(ticket_id, status)

    elif choice == "5":
        ticket_id = input("Ticket ID: ")
        manager.delete_ticket(ticket_id)

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")
