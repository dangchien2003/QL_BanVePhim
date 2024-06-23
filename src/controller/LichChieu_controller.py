import datetime
import sys
import os

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
)

from service.lichchieu_service import LichChieuService

class LichChieuController:
        def __init__(self) :
            self.lichChieuService = LichChieuService()
        
        def layLichChieu(self, timesBegin, timesEnd):
            self.lichChieuService.layLichChieu(timesBegin, timesEnd)
        
