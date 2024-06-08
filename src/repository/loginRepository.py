import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from src.util.excute import Excute


class LoginRepository:
    def __init__(self):
        self.excute = Excute()

    def getStaffByEmail(self, email):
        query = f"SELECT * FROM staff WHERE email = '{email}'"
        return self.excute.getOne(query)
