from src.model.ticket import Ticket
from src.service.ticket_service import TicketService


class TicketController:
    def __init__(self):
        self.ticketService = TicketService()

    def checkInfoTicket(self, ticket: Ticket):
        return self.ticketService.checkInfoTicket(ticket)
