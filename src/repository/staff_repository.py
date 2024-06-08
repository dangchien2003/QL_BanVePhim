import sys
import os

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
)
from util.excute import Excute
from src.model.staff import Staff


class StaffRepository:
    def __init__(self):
        self.excute = Excute()

    def countEmail(self, email):
        query = f"SELECT count(*) FROM staff WHERE email = '{email}'"
        return self.excute.getOne(query)

    def addStaff(self, staff: Staff):
        query = f"INSERT INTO staff(idnv, name, sdt, email, sex, `rank`, password) values('{staff.idnv}', '{staff.name}', '{staff.sdt}', '{staff.email}', '{staff.sex}', '{staff.rank}', '{staff.password}');"
        return self.excute.edit(query)

    def getAll(self):
        query = "SELECT * FROM staff"
        return self.excute.getAll(query)

    def getStaffById(self, id):
        query = f"SELECT * FROM staff WHERE idnv = '{id}'"
        return self.excute.getOne(query)

    def getStaffByName(self, name):
        query = f"SELECT * FROM staff WHERE name like '%{name}%'"
        return self.repository.getAll(query)

    def getStaffByIdOrName(self, id, name):
        query = f"SELECT * FROM staff WHERE name like '%{name}%' or idnv = '{id}'"
        return self.repository.getAll(query)

    def insertBlockAt(self, id, time):
        query = f"UPDATE staff set blockAt = {time} WHERE idnv = '{id}'"
        return self.excute.edit(query)

    def updatePassword(self, id, password):
        query = f"UPDATE staff set password = '{password}' WHERE idnv = '{id}'"
        return self.excute.edit(query)

    def updateInfoStaff(self, staff: Staff):
        query = f"UPDATE staff set name = '{staff.name}', sdt = '{staff.sdt}', email = '{staff.email}', sex = {staff.sex}, `rank` = '{staff.rank}' WHERE idnv = '{staff.idnv}';"
        print(query)
        return self.excute.edit(query)
