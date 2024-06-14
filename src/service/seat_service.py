from src.repository.seat_repository import SeatRepository
from src.util.response import Res


class SeatService:
    def __init__(self):
        self.seatRepository = SeatRepository()
        return

    def getAllSeatOfCalendar(self, idCalendar):
        if idCalendar is None or idCalendar.strip() == "":
            return Res(False, "Id không hợp lệ")

        result = self.seatRepository.getChairSelected(idCalendar)
        if result is None:
            return Res(False, "Lỗi truy vấn")
        return Res(True, data=result)
