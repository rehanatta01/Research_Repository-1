class Ticket:
    ticket_counter = 2000
    tickets = []

    def __init__(self, staff_id, creator_name, contact_email, description):
        self.ticket_id = Ticket.ticket_counter
        Ticket.ticket_counter += 1
        self.staff_id = staff_id
        self.creator_name = creator_name
        self.contact_email = contact_email
        self.description = description
        self.status = "Open"
        self.response = "Not Yet Provided"
        Ticket.tickets.append(self)

    def generate_password(self):
        if "Password Change" in self.description:
            password = self.staff_id[:2] + self.creator_name[:3]
            return password
        return None

    def close_ticket(self, response):
        if self.status != "Closed":
            self.status = "Closed"
            self.response = response

    def reopen_ticket(self):
        if self.status == "Closed":
            self.status = "Reopened"

    @classmethod
    def ticket_stats(cls):
        num_tickets = len(cls.tickets)
        num_resolved_tickets = sum(1 for ticket in cls.tickets if ticket.status == "Closed")
        num_open_tickets = num_tickets - num_resolved_tickets
        return num_tickets, num_resolved_tickets, num_open_tickets

    @classmethod
    def display_all_tickets(cls):
        for ticket in cls.tickets:
            print(f"Ticket Number: {ticket.ticket_id}")
            print(f"Ticket Creator Name: {ticket.creator_name}")
            print(f"Staff ID: {ticket.staff_id}")
            print(f"Email Address: {ticket.contact_email}")
            print(f"Description of the Issue: {ticket.description}")
            print(f"Response from IT Department: {ticket.response}")
            print(f"Ticket Status: {ticket.status}")
            print()

def main():
    # Create at least one ticket with a "Password Change" request
    ticket1 = Ticket("INNAM", "Inna", "inna@whitecliffe.co.nz", "My monitor stopped working")
    ticket2 = Ticket("MARIAH", "Maria", "maria@whitecliffe.co.nz", "Request for a videocamera to conduct webinars")
    ticket3 = Ticket("JOHNS", "John", "john@whitecliffe.co.nz", "Password change")

    # Display ticket statistics
    num_tickets, num_resolved_tickets, num_open_tickets = Ticket.ticket_stats()
    print(f"Displaying Ticket Statistics\n")
    print(f"Tickets Created: {num_tickets}\n")
    print(f"Tickets Resolved: {num_resolved_tickets}\n")
    print(f"Tickets To Solve: {num_open_tickets}\n")

    # Display ticket information
    print("Printing Tickets:\n")
    Ticket.display_all_tickets()

    # Resolve some tickets
    ticket3.close_ticket("New password generated: JOJoh")

    # Display ticket information after resolving some tickets
    print("\nDisplaying Ticket Statistics\n")
    num_tickets, num_resolved_tickets, num_open_tickets = Ticket.ticket_stats()
    print(f"Tickets Created: {num_tickets}\n")
    print(f"Tickets Resolved: {num_resolved_tickets}\n")
    print(f"Tickets To Solve: {num_open_tickets}\n")

    print("Printing Tickets:\n")
    Ticket.display_all_tickets()

if __name__ == "__main__":
    main()


