from src.model.ticket import Ticket
from src.service.ticket_service import TicketService


class TicketController:
    def __init__(self):
        self.ticketService = TicketService()

    def checkInfoTicket(self, ticket: Ticket):
        return self.ticketService.checkInfoTicket(ticket)

    def sendMailTicket(self, idticket, movie, calendar, chairs, customer, to_email):
        return self.ticketService.sendMail(
            idticket, movie, calendar, chairs, customer, to_email
        )

    def getInfoTicket(self, ticket):
        return self.ticketService.getInfoTicket(ticket)

    def checkinTicket(self, ticket, staff):
        return self.ticketService.checkinTicket(ticket, staff)
