import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from src.repository.loginRepository import LoginRepository
from src.util.valid import emailValid, stringValid
from src.util.response import Res
from src.model.staff import Staff
from src.model.staff_current import StaffCurrent
from src.util.encryption.hash import Hash


class LoginService:
    def __init__(self):
        self.loginRepository = LoginRepository()
        self.hash = Hash()

    def adminLogin(self, email, password):
        if emailValid.isEmail(email) is False:
            return Res(False, "Không phải email")
        if stringValid.minLength(string=password, min=1, trim=True) is False:
            return Res(False, "Mật khổng không được trống")

        result = self.loginRepository.getStaffByEmail(email)

        if result is None:
            return Res(False, "Nhân viên không tồn tại")

        staff = Staff(
            idnv=result[0],
            name=result[1],
            sdt=result[2],
            email=result[3],
            sex=result[4],
            rank=result[5],
            blockAt=result[6],
            password=result[7],
        )

        if self.hash.verify(staff.password, password) is False:
            return Res(False, "Mật khẩu không đúng")

        if staff.rank != "admin":
            return Res(False, "Không có quyền truy cập")

        return Res(True)

    def staffLogin(self, email, password):
        if emailValid.isEmail(email) is False:
            return Res(False, "Không phải email")
        if stringValid.minLength(string=password, min=1, trim=True) is False:
            return Res(False, "Mật khổng không được trống")

        result = self.loginRepository.getStaffByEmail(email)

        if result is None:
            return Res(False, "Nhân viên không tồn tại")

        staff = Staff(
            idnv=result[0],
            name=result[1],
            sdt=result[2],
            email=result[3],
            sex=result[4],
            rank=result[5],
            blockAt=result[6],
            password=result[7],
        )

        if self.hash.verify(staff.password, password) is False:
            return Res(False, "Mật khẩu không đúng")

        if staff.rank != "staff":
            return Res(False, "Không có quyền truy cập")

        staffCurrent = StaffCurrent(staff.idnv, staff.name, staff.rank)

        return Res(True, data=staffCurrent)
