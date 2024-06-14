from src.repository.calendar_repository import CalendarRepository
from src.repository.movie_repository import MovieRepository
from src.util.response import Res
from src.util.genarate import gen_time
from src.util import time


class CalendarService:
    def __init__(self):
        self.calendarRepository = CalendarRepository()
        return

    def getCalendarByIdmovieAndDate(self, idMovie, date) -> Res:
        timestampInput = time.convertTimeToTimestamp(date, "%d-%m-%Y")
        if timestampInput is None:
            return Res(False, "Lỗi chuyển thời gian")

        now = gen_time.getNowTimestamp()

        timeStart = None

        if timestampInput < now:
            timeStart = now
        else:
            timeStart = timestampInput

        result = self.calendarRepository.getCalendarOfMovie(idMovie, timeStart)

        if result is None:
            return Res(False, "Lỗi truy vấn")
        return Res(True, data=result)

    def getRemaingMovieByIdCalendar(self, idCalendar):
        if idCalendar is None or idCalendar.strip() == "":
            return Res(False, "Id không hợp lệ")

        result = self.calendarRepository.getRemaingMovieByIdCalendar(idCalendar)

        if result is None:
            return Res(False, "Lỗi truy vấn")

        return Res(True, data=result)
