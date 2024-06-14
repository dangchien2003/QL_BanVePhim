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
