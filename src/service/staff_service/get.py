import sys
import os

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
)
from src.util.response import Res
from src.repository.staff_repository import StaffRepository
from src.util.staff import StaffUtil
from src.model.staff import Staff
from src.model.staff_current import StaffCurrent
from src.util.valid import emailValid
from src.util.encryption.hash import Hash


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

    def staffLogin(self, email, password) -> Res:
        if emailValid.isEmail(email) is False:
            return Res(False, "Email không hợp lệ")

        if password.strip() == "":
            return Res(False, "Không có mật khẩu")

        staffTuple = self.staffRepository.getStaffByEmail(email)

        if staffTuple is None:
            return Res(False, "Không tồn tại nhân viên trong hệ thống")

        staffList = list(staffTuple)
        passwordDb = staffList[7]

        staff = Staff(
            idnv=staffList[0],
            name=staffList[1],
            sdt=staffList[2],
            email=staffList[3],
            sex=staffList[4],
            rank=staffList[5],
            blockAt=staffList[6],
            password=staffList[7],
        )

        hash = Hash()
        if hash.verify(staff.password, password) is False:
            return Res(False, "Mật khẩu sai")

        if staff.blockAt is not None:
            return Res(False, "Tài khoản đã bị khoá")

        if staff.rank != "staff":
            return Res(False, "Không có quyền truy cập")

        staffCurrent = StaffCurrent(staff.idnv, staff.name, staff.rank)

        return Res(True, data=staffCurrent)
