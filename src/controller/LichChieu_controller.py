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

    def searchTimKiem(self, date, selected_room):
        return self.lichChieuService.searchTimKiem(date, selected_room)
    def fetch_movie(self):
        return self.lichChieuService.get_all_movie()

        
