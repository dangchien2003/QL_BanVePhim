from src.util.excute import Excute


class CalendarRepository:
    def __init__(self):
        self.excute = Excute()

    def getCalendarOfMovie(self, idMovie, timeStart):
        query = f"""SELECT 
                        calendar.id, 
                        calendar.time 
                    FROM calendar 
                    JOIN
                        movie
                    ON
                        movie.id = calendar.idMovie
                    WHERE 
                        idMovie = '{idMovie}'
                    AND
                        calendar.cancleAt IS NULL
                    AND
                        calendar.time + movie.time*60 - 1800  BETWEEN {timeStart} AND calendar.time + movie.time*60 - 1800"""
        return self.excute.getAll(query)

    def getRemaingMovieByIdCalendar(self, idCalendar):
        query = f"""SELECT 
                        movie.time AS timeMovie,
                        calendar.time AS playTime,
                        calendar.room
                    FROM calendar
                    JOIN
                        movie
                    ON
                        movie.id = calendar.idMovie
                    WHERE 
                        calendar.id = '{idCalendar}'"""
        return self.excute.getOne(query)
