from src.service.tkphim_service import TkPhimService


class TkPhimController:
    def __init__(self):
        self.tkPhimService = TkPhimService()

    def thongke(self, style, phim, ngay, thang, nam):
        return self.tkPhimService.fillter(style, phim, ngay, thang, nam)
