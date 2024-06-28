import sys
import os

from util.excute import Excute

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
)


class LichChieuRepository:
    def __init__(self):
        self.excute = Excute()

    def searchTimKiem(self, start_timestamp, end_timestamp, room):
        query = f"SELECT calendar.time as timeCalendar, calendar.room,  movie.name, movie.time as timeMovie, calendar.id FROM calendar join movie on calendar.idMovie = movie.id where calendar.time between {start_timestamp} and {end_timestamp} and calendar.room = {room} and calendar.cancleAt is null;"

        return self.excute.getAll(query)

    def fetch_all_movie_names(self):
        query = (
            f"select movie.id, movie.name, movie.time from movie"
        )
        return self.excute.getAll(query)

    def get_all_calendar(self, start, end, room):
        query = f"select calendar.id from calendar join movie on movie.id = calendar.idMovie where calendar.room = {room} and (calendar.time + movie.time*60) between {start} and {end}"
        return self.excute.getAll(query)

    def add_calendar(self, id, movie, start, room):
        query = f"insert into calendar(id, idMovie, time, room) values('{id}','{movie}', {start}, {room})"
        return self.excute.edit(query)

    def updateCancleAt(self, id, time):
        query = f"update calendar set cancleAt = {time} where id = '{id}' and cancleAt is null"
        return self.excute.edit(query)

    def updateCalendar(self, id, movie, start, room):
        query = f"update calendar set idMovie = '{movie}', time = {start}, room = '{room}' where id = '{id}'"
        return self.excute.edit(query)
