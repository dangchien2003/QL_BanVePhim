import calendar
from src.util import time
from src.util.response import Res

from src.repository.tkphim_repository import TkPhimRepository


class TkPhimService:
    def __init__(self):
        self.Repository = TkPhimRepository()
        return

    def fillter(self, style, phim, ngay, thang, nam):
        start_timestamp = 0
        end_timestamp = 0
        if style == 1:

            start_timestamp = time.convertTimeToTimestamp(
                f"{ngay}-{thang}-{nam}", "%d-%m-%Y"
            )
            end_timestamp = start_timestamp + 86400
        elif style == 2:
            start_timestamp = time.convertTimeToTimestamp(f"{thang}-{nam}", "%m-%Y")
            days = calendar.monthrange(nam, thang)[1]
            end_timestamp = start_timestamp + 86400 * days
        elif style == 3:
            start_timestamp = time.convertTimeToTimestamp(f"{nam}", "%Y")
            days = 366 if calendar.isleap(nam) else 365
            end_timestamp = start_timestamp + 86400 * days
        else:
            return Res(False, "Không hỗ trợ, vui lòng nhập lại")

        result = self.Repository.getInfo(phim, start_timestamp, end_timestamp)
        if result is None:
            return Res(False, "Lỗi truy vấn dữ liệu")
        if len(result) == 0:
            return Res(False, "Không có dữ liệu")

        ketQuaThongKe = None

        if style == 1:
            ketQuaThongKe = self.thongKeNgay(result)
        elif style == 2:
            ketQuaThongKe = self.thongKeThang(result)
        elif style == 3:
            ketQuaThongKe = self.thongKeNam(result)

        return Res(True, data=ketQuaThongKe)

    def thongKeNgay(self, data):
        sove = doanhthu = 0
        result = []
        for item in data:
            sove += 1
            doanhthu += item[1]

        date = time.convertTimeStampToString(data[0][0], "%d-%m-%Y")

        result.append({"date": date, "soVe": sove, "doanhThu": doanhthu})
        return result

    def thongKeThang(self, data):
        day = time.convertTimeStampToString(data[0][0], "%d")
        result = []
        # Tính toán doanh thu cho từng ngày
        sove = doanhthu = 0
        date = time.convertTimeStampToString(data[0][0], "%d-%m-%Y")
        for item in data:
            dayItem = time.convertTimeStampToString(item[0], "%d")
            if dayItem == day:
                sove += 1
                doanhthu += item[1]
            else:

                result.append({"date": date, "soVe": sove, "doanhThu": doanhthu})
                date = time.convertTimeStampToString(item[0], "%d-%m-%Y")
                day = dayItem
                doanhthu = item[1]
                sove = 1

        result.append({"date": date, "soVe": sove, "doanhThu": doanhthu})
        return result

    def thongKeNam(self, data):
        month = time.convertTimeStampToString(data[0][0], "%m")
        result = []
        # Tính toán doanh thu cho từng ngày
        sove = doanhthu = 0
        date = time.convertTimeStampToString(data[0][0], "%m-%Y")
        for item in data:
            monthItem = time.convertTimeStampToString(item[0], "%m")
            if monthItem == month:
                sove += 1
                doanhthu += item[1]
            else:
                result.append({"date": date, "soVe": sove, "doanhThu": doanhthu})
                date = time.convertTimeStampToString(item[0], "%m-%Y")
                month = monthItem
                doanhthu = item[1]
                sove = 1

        result.append({"date": date, "soVe": sove, "doanhThu": doanhthu})
        return result
