import sys
import os

from util.excute import Excute
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
)

class LichChieuRepository:
    def __init__(self):
        self.excute = Excute()

    def layDuLieuChoBang(self):
        query = "select calendar.id,  movie.name, calendar.time, calendar.room from calendar join movie on movie.id = calendar.idMovie"
        return self.excute.getAll(query)