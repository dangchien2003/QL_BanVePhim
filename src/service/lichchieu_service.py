import sys
import os

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
)

from src.repository.lichchieu_repository import LichChieuRepository
from src.util.Lichchieu import LichchieuUtil
from src.util.response import Res

class LichChieuService:
    def __init__(self):
        self.lichChieuRepository = LichChieuRepository()
        self.LichchieuUtil = LichchieuUtil()

    def layLichChieu(self, timesBegin, timesEnd):
        if timesBegin

  