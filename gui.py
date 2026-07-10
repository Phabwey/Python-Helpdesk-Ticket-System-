import tkinter as tk
from tkinter import messagebox
from ticket_manager import TicketManager

manager = TicketManager()


def create_ticket():
    ticket_id = ticket_id_entry.get()
    customer_name = customer_name_entry.get()
    issue = issue_entry.get()
    category = category_var.get()
    technician = technician_entry.get()
    priority = priority_var.get()

    if not all(
        [ticket_id, customer_name, issue, category, technician, priority]
    ):
        messagebox.showerror(
            "Error",
            "Please fill in all fields."
        )
        return

    manager.create_ticket(
        ticket_id,
        customer_name,
        issue,
        priority,
        category,
        technician
    )

    messagebox.showinfo(
        "Success",
        "Ticket created successfully!"
    )

    ticket_id_entry.delete(0, tk.END)
    customer_name_entry.delete(0, tk.END)
    issue_entry.delete(0, tk.END)
    technician_entry.delete(0, tk.END)


root = tk.Tk()
root.title("Python Helpdesk Ticket System")
root.geometry("500x500")

tk.Label(root, text="Ticket ID").pack()
ticket_id_entry = tk.Entry(root)
ticket_id_entry.pack()

tk.Label(root, text="Customer Name").pack()
customer_name_entry = tk.Entry(root)
customer_name_entry.pack()

tk.Label(root, text="Issue").pack()
issue_entry = tk.Entry(root)
issue_entry.pack()

tk.Label(root, text="Category").pack()

category_var = tk.StringVar(root)
category_var.set("Hardware")

category_menu = tk.OptionMenu(
    root,
    category_var,
    "Hardware",
    "Software",
    "Network"
)

category_menu.pack()

tk.Label(root, text="Assigned Technician").pack()
technician_entry = tk.Entry(root)
technician_entry.pack()

tk.Label(root, text="Priority").pack()

priority_var = tk.StringVar(root)
priority_var.set("Low")

priority_menu = tk.OptionMenu(
    root,
    priority_var,
    "Low",
    "Medium",
    "High"
)

priority_menu.pack()

tk.Button(
    root,
    text="Create Ticket",
    command=create_ticket
).pack(pady=20)

root.mainloop()
