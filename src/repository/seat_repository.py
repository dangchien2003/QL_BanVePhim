from src.util.excute import Excute


class SeatRepository:
    def __init__(self):
        self.excute = Excute()

    def getChairSelected(self, idCalendar):
        query = f"""SELECT
                        seat.location
                    FROM seat
                    JOIN calendar
                    ON calendar.id = seat.idCalendar
                    WHERE seat.idCalendar = '{idCalendar}'"""
        return self.excute.getAll(query)

    def orderSeat(self, data):
        query = f"INSERT INTO seat(idTicket, idCalendar, location) values(%s, %s, %s)"
        return self.excute.editMany(query, data)

    def getInfoSeat(self, ticket):
        query = f"select location from seat where idTicket = '{ticket}'"
        return self.excute.getMany(query, 100)
