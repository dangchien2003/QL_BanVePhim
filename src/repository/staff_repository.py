import sys
import os

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
)
from util.excute import Excute
from src.model.staff import Staff


class StaffRepository:
    def __init__(self):
        self.repository = Excute()

    def countEmail(self, email):
        query = f"SELECT count(*) FROM staff WHERE email = '{email}'"
        return self.repository.getOne(query)

    def addStaff(self, staff: Staff):
        query = f"INSERT INTO staff(idnv, name, sdt, email, sex, `rank`, password) values('{staff.idnv}', '{staff.name}', '{staff.sdt}', '{staff.email}', '{staff.sex}', '{staff.rank}', '{staff.password}');"
        print(query)

        return self.repository.edit(query)
