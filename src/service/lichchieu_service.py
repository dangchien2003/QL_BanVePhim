import sys
import os
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
)

from src.repository.lichchieu_repository import LichChieuRepository
from src.util.Lichchieu import LichchieuUtil
from src.util.response import Res
from src.util import time

class LichChieuService:
    def __init__(self):
        self.lichChieuRepository = LichChieuRepository()
        self.LichchieuUtil = LichchieuUtil()

    def searchTimKiem(self, date, selected_room):
        start_timestamp = time.convertTimeToTimestamp(f"{date}", "%d/%m/%Y")
        end_timestamp = start_timestamp + 86400 
        roomlist = selected_room.split()
        room = roomlist[1]
        data = self.lichChieuRepository.searchTimKiem(start_timestamp, end_timestamp, room)
        list = []

        for item in data:
            nameMovie = item[2]
            room = item[1]
            day = time.convertTimeStampToString(item[0], "%d/%m/%Y")
            timeStart = time.convertTimeStampToString(item[0], "%H:%M")
            timeEnd = time.convertTimeStampToString(item[0] + item[3]*60, "%H:%M")
            itemList = {
                "name": nameMovie,
                "room": room,
                "day": day,
                "timestart" : timeStart,
                "timeend": timeEnd
            }
            list.append(itemList)
        if len(list) ==0:
            return Res(False, message="Không có dữ liệu")
        
        return Res(success=True, data=list)
    def get_all_movie(self):
        data = self.lichChieuRepository.fetch_all_movie_names()
        if(data is None):
            return Res(False, "Lỗi truy vấn dữ liệu")
        movies = []
        for item in data:
            movie = {
                "id": item[0],
                "name": item[1]
            }
            movies.append(movie)
        return Res(success=True, data=movies)
    

       