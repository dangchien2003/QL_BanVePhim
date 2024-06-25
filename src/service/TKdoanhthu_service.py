import sys
import os
import calendar
from src.util import time
from src.util.response import Res
from src.repository.TKdoanhthu_reponsitory import TKdoanhthuRepository
from src.model.dulieudoanhthu import DuLieuDoanhThu


class GetTKdoanhthu_Service:

    def __init__(self):
        self.Repository = TKdoanhthuRepository()
        return

    def fillter(self, style, day, month, year):
        start_timestamp = 0
        end_timestamp = 0
        if style == 1:

            start_timestamp = time.convertTimeToTimestamp(
                f"{day}-{month}-{year}", "%d-%m-%Y"
            )
            end_timestamp = start_timestamp + 86400
        elif style == 2:
            start_timestamp = time.convertTimeToTimestamp(f"{month}-{year}", "%m-%Y")
            days = calendar.monthrange(year, month)[1]
            end_timestamp = start_timestamp + 86400 * days
        elif style == 3:
            start_timestamp = time.convertTimeToTimestamp(f"{year}", "%Y")
            days = 366 if calendar.isleap(year) else 365
            end_timestamp = start_timestamp + 86400 * days
        else:
            return Res(False, "Không hỗ trợ, vui lòng nhập lại")
        result = self.Repository.getInfo(start_timestamp, end_timestamp)
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
        doanhthuve = doanhthunuoc = doanhthubong = 0
        array = []
        for item in data:
            doanhthuve += item[1]
            doanhthunuoc += item[2]
            doanhthubong += item[3]

        sum = doanhthuve + doanhthunuoc + doanhthubong
        date = time.convertTimeStampToString(data[0][0], "%d-%m-%Y")

        array.append(DuLieuDoanhThu(date, doanhthuve, doanhthunuoc, doanhthubong, sum))
        return array

    def thongKeThang(self, data):
        day = time.convertTimeStampToString(data[0][0], "%d")
        result = []
        # Tính toán doanh thu cho từng ngày
        doanhthuve = doanhthunuoc = doanhthubong = 0
        date = time.convertTimeStampToString(data[0][0], "%d-%m-%Y")
        for item in data:
            dayItem = time.convertTimeStampToString(item[0], "%d")
            if dayItem == day:
                doanhthuve += item[1]
                doanhthunuoc += item[2]
                doanhthubong += item[3]
            else:
                sum = doanhthuve + doanhthunuoc + doanhthubong
                result.append(
                    DuLieuDoanhThu(date, doanhthuve, doanhthunuoc, doanhthubong, sum)
                )
                date = time.convertTimeStampToString(item[0], "%d-%m-%Y")
                day = dayItem
                doanhthuve = item[1]
                doanhthunuoc = item[2]
                doanhthubong = item[3]
        sum = doanhthuve + doanhthunuoc + doanhthubong
        result.append(DuLieuDoanhThu(date, doanhthuve, doanhthunuoc, doanhthubong, sum))

        return result

    def thongKeNam(self, data):
        month = time.convertTimeStampToString(data[0][0], "%m")
        result = []
        # Tính toán doanh thu cho từng ngày
        doanhthuve = doanhthunuoc = doanhthubong = 0
        date = time.convertTimeStampToString(data[0][0], "%m-%Y")
        for item in data:
            monthItem = time.convertTimeStampToString(item[0], "%m")
            if monthItem == month:
                doanhthuve += item[1]
                doanhthunuoc += item[2]
                doanhthubong += item[3]
            else:
                sum = doanhthuve + doanhthunuoc + doanhthubong
                result.append(
                    DuLieuDoanhThu(date, doanhthuve, doanhthunuoc, doanhthubong, sum)
                )
                date = time.convertTimeStampToString(item[0], "%m-%Y")
                month = monthItem
                doanhthuve = item[1]
                doanhthunuoc = item[2]
                doanhthubong = item[3]
        sum = doanhthuve + doanhthunuoc + doanhthubong
        result.append(DuLieuDoanhThu(date, doanhthuve, doanhthunuoc, doanhthubong, sum))
        return result
