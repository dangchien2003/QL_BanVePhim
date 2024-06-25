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
        query = f"SELECT calendar.time as timeCalendar, calendar.room,  movie.name, movie.time as timeMovie FROM calendar join movie on calendar.idMovie = movie.id where calendar.time between {start_timestamp} and {end_timestamp} and calendar.room = {room} and calendar.cancleAt is null;"
       
        return self.excute.getAll(query)
    
    def fetch_all_movie_names(self):
        query = f"select movie.id, movie.name from movie where hideAt is null"
        return self.excute.getAll(query)
    