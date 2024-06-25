from src.util.excute import Excute


class TkPhimRepository:
    def __init__(self):
        self.excute = Excute()

    def getInfo(self, movie, start_timestamp, end_timestamp):
        query = f"select ticket.createAt, priceTicket from ticket join calendar on calendar.id = ticket.idCalendar join movie on calendar.idMovie = movie.id where ticket.createAt between {start_timestamp} and {end_timestamp} and idMovie = '{movie}' order by ticket.createAt"
        return self.excute.getAll(query)
