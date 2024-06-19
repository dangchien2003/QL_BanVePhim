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
from src.service.render_template_service import RenderHtml
from src.service.mail_service import MailService


class AddService:
    def __init__(self):
        self.staffRepository = StaffRepository()
        self.hash = Hash()
        self.render = RenderHtml()
        self.mail = MailService()

    def checkEmail(self, email):
        if emailValid.isEmail(email) is False:
            return Res(False, "Email không hợp lệ")

        if self.staffRepository.countEmail(email)[0] > 0:
            return Res(False, "Email đã tồn tại")

        return Res(True)

    def checkPassword(self, password):
        if len(password.strip()) != len(password):
            return Res(False, "Chứa space đầu hoặc cuối")

        if len(password) < 8:
            return Res(False, "Mật khẩu quá ngắn")

        return Res(True)

    def getNewId(self):
        now = int(gen_time.getNowTimestamp())
        randomNumber = gen_number.genarateNumber(3)
        return f"STAFF_{now}_{randomNumber}"

    def convertRank(self, rankStr: str):
        newRank = rankStr.lower()
        if newRank == "staff" or newRank == "admin":
            return newRank
        return None

    def addStaff(self, staff: Staff, passwordStr):
        if staff.name.strip() == "" or staff.name is None:
            return Res(False, "Thiếu trường tên")
        if staff.sdt.strip() == "" or staff.sdt is None:
            return Res(False, "Thiếu trường sđt")
        insert = self.staffRepository.addStaff(staff)
        if insert == 0:
            return Res(False, "Thêm thất bại")
        content = {
            "name": staff.name,
            "email": staff.email,
            "password": passwordStr,
        }
        body = self.render.generate_html("mail_create_staff.html", content)
        if (
            self.mail.SendMail("Cung cấp tài khoản làm việc", body, staff.email)
            is False
        ):
            print("Lỗi gửi mail")
        return Res(True)
