import sys
import os

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
)
from src.util.valid import emailValid
from src.util.response import Res
from src.repository.staff_repository import StaffRepository
from src.util.encryption.hash import Hash
from src.util.genarate.gen_string import generatePassword
from src.util.genarate import gen_number, gen_time
from src.model.staff import Staff


class EditService:
    def __init__(self):
        self.staffRepository = StaffRepository()

    def blockStaff(self, id):
        if len(id.strip()) < 5:
            return Res(False, "Id không hợp lệ")

        now = gen_time.getNowTimestamp()

        result = self.staffRepository.insertBlockAt(id, now)
        if result == 0:
            return Res(False, "Khoá tài khoản thất bại")

        return Res(True)

    def updateRandomPassword(self, id, password):
        if len(id) < 5:
            return Res(False, "Id không hợp lệ")
        if password == "":
            return Res(False, "Mật khẩu không hợp lệ")

        result = self.staffRepository.updatePassword(id, password)

        if result == 0:
            return Res(False, "Thay đổi thất bại")

        return Res(True, "Thay đổi thành công")

    def updateInfo(self, staff: Staff):
        if len(staff.idnv.strip()) < 5:
            return Res(False, "Id không hợp lệ")

        if staff.sex != 0 and staff.sex != 1:
            return Res(False, "Giới tính không hợp lệ")

        staff.rank = staff.rank.strip().lower()

        if staff.rank != "staff":
            return Res(False, "Quyền không tồn tại")

        if len(staff.name.strip()) == 0:
            return Res(False, "Tên không hợp lệ")

        if (emailValid.isEmail(staff.email)) is False:
            return Res(False, "Email không hợp lệ")

        update = self.staffRepository.updateInfoStaff(staff)
        if update == 0:
            return Res(False, "Cập nhật thất bại")

        return Res(True)
