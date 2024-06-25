import sys
import os

from util.response import Res


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from src.service.TKdoanhthu_service import GetTKdoanhthu_Service


class TKdoanhthu_controller:
    def __init__(self):
        self.getTKdoanhthu_Service = GetTKdoanhthu_Service()

    # def getData(self, style, day, month, year):
    #     return self.getTKdoanhthu_Service.fillter(style, day, month, year)

    def getData(self, style, day, month, year):
        return self.getTKdoanhthu_Service.fillter(style, day, month, year)
