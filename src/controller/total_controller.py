from src.service.total_Service import TotalService
from src.util.response import Res


class TotalController:
    def __init__(self):
        self.totalService = TotalService()

    def cal_totalTicket(self, selecting: list, priceFirstRow: int) -> Res:
        return self.totalService.cal_totalTicket(selecting, priceFirstRow)

    def cal_totalPopcorn(self, quantity: int):
        return self.totalService.cal_totalPopcorn(quantity)

    def cal_totalWater(self, quantity: int):
        return self.totalService.cal_totalWater(quantity)
