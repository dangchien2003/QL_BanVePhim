import sys
import os

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
)

from src.service.login.login_service import LoginService


class LoginController:
    def __init__(self, login):
        self.login = login
        self.LoginService = LoginService()

    def loginByAdmin(self):
        return self.LoginService.adminLogin(self.login.email, self.login.password)

    def loginByStaff(self):
        return self.LoginService.staffLogin(self.login.email, self.login.password)
