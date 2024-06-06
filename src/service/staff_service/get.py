import sys
import os

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
)
from util.response import Res
from repository.staff_repository import StaffRepository
from src.util.staff import StaffUtil
from src.model.staff import Staff


class GetService:
    def __init__(self):
        self.staffRepository = StaffRepository()
        self.staffUtil = StaffUtil()

    def getAllStaffNormal(self):
        staffs = self.staffRepository.getAll()
        return self.staffUtil.getInfoTableFromArray(staffs)

    def getStaffById(self, id: str):
        if len(id) < 5:
            return Res(False, "Id không hợp lệ")

        result = self.staffRepository.getStaffById(id)

        if result is None:
            return Res(False, "Không tìm thấy thông tin")

        return Res(
            True,
            data=Staff(
                result[0],
                result[1],
                result[2],
                result[3],
                result[4],
                result[5],
                result[6],
                result[7],
            ),
        )

    def getStaffById(self, id: str):
        if len(id) < 5:
            return Res(False, "Id không hợp lệ")

        result = self.staffRepository.getStaffById(id)

        if result is None:
            return Res(False, "Không tìm thấy thông tin")

        return Res(
            True,
            data=Staff(
                result[0],
                result[1],
                result[2],
                result[3],
                result[4],
                result[5],
                result[6],
                result[7],
            ),
        )

    def findStaff(self, id, name):
        if id == "" and name == "":
            return Res(False, "Dữ liệu không hợp lệ")

        if id != "" and name != "":
            result = self.staffRepository.getStaffByIdOrName(id, name)

            if len(result) == 0:
                return Res(False, "Không tìm thấy thông tin")

            return Res(True, data=self.staffUtil.getInfoTableFromArray(result))

        if id != "":
            result = self.staffRepository.getStaffById(id)

            if result is None:
                return Res(False, "Không tìm thấy thông tin")

            return Res(True, data=[self.staffUtil.getInfoTable(result)])

        if name != "":
            result = self.staffRepository.getStaffByName(name)

            if result is None:
                return Res(False, "Không tìm thấy thông tin")

            return Res(True, data=self.staffUtil.getInfoTableFromArray(result))
