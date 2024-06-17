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

    def getInfoTicket(self, ticket):
        query = f"select ticket.id, calendar.time, calendar.room, ticket.numPerson, ticket.numPopcorn, ticket.numWater, ticket.checkinAt, movie.time from ticket join calendar on calendar.id = ticket.idCalendar join movie on calendar.idMovie = movie.id where ticket.id = '{ticket}'"
        return self.excute.getMany(query, 1)

    def checkin(self, ticket, time, staff):
        query = f"update ticket set checkinAt = '{time}', checkinBy = '{staff}'where id = '{ticket}'"
        return self.excute.edit(query)
