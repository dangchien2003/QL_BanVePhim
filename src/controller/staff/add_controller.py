import sys
import os

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
)

from src.service.staff_service.add import AddService
from src.util.genarate.gen_string import generatePassword
from src.util.encryption.hash import Hash


class AddStaffController:
    def __init__(self):
        self.addStaffService = AddService()

    def checkEmail(self, email):
        return self.addStaffService.checkEmail(email)

    def checkPassword(self, password):
        return self.addStaffService.checkPassword(password)

    def getNewPassword(self):
        return generatePassword(10)

    def getNewId(self):
        return self.addStaffService.getNewId()

    def convertRank(self, rank: str):
        return self.addStaffService.convertRank(rank)

    def add(self, staff):
        return self.addStaffService.addStaff(staff)

    def convertHashPasswords(self, password: str):
        return Hash().getHash(password)
