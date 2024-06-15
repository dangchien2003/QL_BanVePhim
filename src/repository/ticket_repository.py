from src.model.ticket import Ticket
from src.util.excute import Excute


class TicketRepository:
    def __init__(self):
        self.excute = Excute()

    def orderTicket(self, ticket: Ticket, idStaff):
        query = f"""
        INSERT INTO 
            `ticket_manager`.`ticket` (`id`, `idCalendar`, `name`, `email`, `numPerson`, `numPopcorn`, `numWater`, `priceTicket`, `pricePopcorn`, `priceWater`, `createBy`, `createAt`) 
        VALUES 
            ('{ticket.id}', '{ticket.calendar}', '{ticket.name}', '{ticket.email}', '{ticket.numPerson}', '{ticket.numPopcorn}', '{ticket.numWater}', '{ticket.priceTicket}', '{ticket.pricePopcorn}', '{ticket.priceWater}', '{idStaff}', '{ticket.createAt}');"""
        return self.excute.edit(query)
