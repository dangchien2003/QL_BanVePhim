import sys
import os

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
)

from src.repository.lichchieu_repository import LichChieuRepository
from src.util.Lichchieu import LichchieuUtil
from src.util.response import Res
from src.util import time
from src.util.genarate import gen_time, gen_number
from src.repository.movie_repository import MovieRepository


class LichChieuService:
    def __init__(self):
        self.lichChieuRepository = LichChieuRepository()
        self.movieRepository = MovieRepository()
        self.LichchieuUtil = LichchieuUtil()

    def searchTimKiem(self, date, selected_room):
        start_timestamp = time.convertTimeToTimestamp(f"{date}", "%d/%m/%Y")
        end_timestamp = start_timestamp + 86400
        roomlist = selected_room.split()
        room = roomlist[1]
        data = self.lichChieuRepository.searchTimKiem(
            start_timestamp, end_timestamp, room
        )
        list = []

        for item in data:
            nameMovie = item[2]
            room = item[1]
            date = time.convertTimeStampToString(item[0], "%d/%m/%Y")
            day = time.convertTimeStampToString(item[0], "%d")
            month = time.convertTimeStampToString(item[0], "%m")
            year = time.convertTimeStampToString(item[0], "%Y")
            timeStart = time.convertTimeStampToString(item[0], "%H:%M")
            hStart = time.convertTimeStampToString(item[0], "%H")
            mStart = time.convertTimeStampToString(item[0], "%M")
            timeEnd = time.convertTimeStampToString(item[0] + item[3] * 60, "%H:%M")
            id = item[4]
            itemList = {
                "name": nameMovie,
                "room": room,
                "date": date,
                "timestart": timeStart,
                "timeend": timeEnd,
                "id": id,
                "day": day,
                "month": month,
                "year": year,
                "hourStart": hStart,
                "minuteStart": mStart,
            }
            list.append(itemList)
        if len(list) == 0:
            return Res(False, message="Không có dữ liệu")

        return Res(success=True, data=list)

    def get_all_movie(self):
        data = self.lichChieuRepository.fetch_all_movie_names()
        if data is None:
            return Res(False, "Lỗi truy vấn dữ liệu")
        movies = []
        for item in data:
            movie = {"id": item[0], "name": item[1], "time": item[2]}
            movies.append(movie)
        return Res(success=True, data=movies)

    def add_lichchieu(self, movie, room: str, datetime):

        playAt = int(time.convertTimeToTimestamp(datetime, "%H:%M %d/%m/%Y"))
        if playAt < gen_time.getNowTimestamp():
            return Res(False, "Thời gian chiếu không hợp lệ")
        movies = self.movieRepository.findMovieById(movie)
        if len(movies) == 0:
            return Res(False, "Phim không đúng")

        infoMovie = movies[0]
        timeMovie = infoMovie[4]
        endPlay = playAt + timeMovie * 60
        roomId = room.split()[1]
        calendars = self.lichChieuRepository.get_all_calendar(
            playAt - 15 * 60, endPlay, roomId
        )

        if calendars is None:
            return Res(False, "Lỗi truy vấn")

        if len(calendars) > 0:
            return Res(False, "Trùng lịch chiếu")

        id = (
            f"CALENDAR_{int(gen_time.getNowTimestamp())}_{gen_number.genarateNumber(3)}"
        )

        inserted = self.lichChieuRepository.add_calendar(id, movie, playAt, roomId)
        if inserted == 0:
            return Res(False, "Thêm thất bại")

        return Res(True)

    def cancle(self, id):
        if id.strip() == "":
            return Res(False, "Id không hợp lệ")

        updated = self.lichChieuRepository.updateCancleAt(
            id, int(gen_time.getNowTimestamp())
        )

        if updated == 0:
            return Res(False, "Thay đổi thất bại")

        return Res(True)

    def edit(self, id, movie, room, datetime):
        if id.strip() == "":
            return Res(False, "Id không hợp lệ")
        playAt = int(time.convertTimeToTimestamp(datetime, "%H:%M %d/%m/%Y"))
        if playAt < gen_time.getNowTimestamp():
            return Res(False, "Thời gian chiếu không hợp lệ")
        movies = self.movieRepository.findMovieById(movie)
        if len(movies) == 0:
            return Res(False, "Phim không đúng")
        infoMovie = movies[0]
        timeMovie = infoMovie[4]
        endPlay = playAt + timeMovie * 60
        roomId = room.split()[1]
        calendars = self.lichChieuRepository.get_all_calendar(
            playAt - 15 * 60, endPlay, roomId
        )

        if calendars is None:
            return Res(False, "Lỗi truy vấn")

        if len(calendars) > 1:
            return Res(False, "Trùng lịch chiếu")

        if len(calendars) == 1:
            calendar = calendars[0]
            if calendar[0] != id:
                return Res(False, "Trùng lịch chiếu")

        updated = self.lichChieuRepository.updateCalendar(id, movie, playAt, roomId)

        if updated == 0:
            return Res(False, "Thay đổi thất bại")

        return Res(True)
