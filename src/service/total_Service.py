import os
from bean import load_env
from src.util.response import Res
from src.util import _string, number


class TotalService:
    def cal_totalTicket(self, selecting: list, priceFirstRow: int):
        if len(selecting) == 0 or priceFirstRow <= 0:
            return "Dữ liệu không hợp lệ"
        row = None
        position = 0
        total = 0
        for chair in selecting:
            if row is None or chair[0] != row:
                row = chair[0]
                position = _string.getPositionChar(row)
                if position is None:
                    return Res(False, "Mã ghế không hợp lệ")
            total += priceFirstRow + priceFirstRow * (5 / 100) * (position - 1)
        return Res(True, data=number.convertPrice(total))

    def cal_totalPopcorn(self, quantity: int):
        priceOnePopcorn = None
        try:
            priceOnePopcorn = int(os.getenv("PRICE_POPCORN"))
        except:
            print("Lỗi lấy giá trị bắp rang bơ")

        if priceOnePopcorn is None:
            return Res(False, "Không thể lấy giá bắp rang")
        total_number = quantity * priceOnePopcorn
        total_money = number.convertPrice(total_number)
        dataRes = {"total_money": total_money, "total_number": total_number}
        return Res(True, data=dataRes)

    def cal_totalWater(self, quantity: int):
        priceOneWater = None
        try:
            priceOneWater = int(os.getenv("PRICE_WATER"))
        except:
            print("Lỗi lấy giá trị nước")

        if priceOneWater is None:
            return Res(False, "Không thể lấy giá nước")
        total_number = quantity * priceOneWater
        total_money = number.convertPrice(total_number)
        dataRes = {"total_money": total_money, "total_number": total_number}
        return Res(True, data=dataRes)
