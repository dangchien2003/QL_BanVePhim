from src.service.tkveban_service import Tkveban_Service


class TKveban_controller:
    def __init__(self):
        self.getTKveban_Service = Tkveban_Service()

    def getData(self, style, day, month, year):
        return self.getTKveban_Service.fillter(style, day, month, year)
