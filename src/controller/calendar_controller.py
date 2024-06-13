from src.service.calendar_service import CalendarService
from src.util.response import Res


class CalendarController:
    def __init__(self):
        self.calendarService = CalendarService()

    def getCalendar(self, idMovie, date) -> Res:
        return self.calendarService.getCalendarByIdmovieAndDate(idMovie, date)

    def getRemaingMovie(self, idCalendar) -> Res:
        return self.calendarService.getRemaingMovieByIdCalendar(idCalendar)
