import smtplib
import ssl
import os
import multiprocessing

# import bean.load_env
from email.message import EmailMessage


class MailService:
    def getMail(self):
        try:
            self.email = os.environ.get("EMAIL")
            self.personal = os.environ.get("PERSONAL")
            self.password = os.environ.get("PASSWORD")
            if (
                self.email == ""
                or self.personal == ""
                or self.password == ""
                or self.email == None
                or self.personal == None
                or self.password == None
            ):
                return False
            return True
        except Exception as e:
            print(e)
            return False

    def SendMail(self, subject, body, to_email):
        if (self.getMail()) is False:
            print("Lỗi lấy thông tin mail")
            return False

        process1 = multiprocessing.Process(
            target=self.send, args=(subject, body, to_email)
        )
        process1.start()
        return True

    def send(self, subject, body, to_email):
        msg = EmailMessage()
        msg["From"] = self.personal
        msg["To"] = to_email
        msg["Subject"] = subject
        msg.set_content(body, subtype="html")

        context = ssl.create_default_context()

        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                server.login(self.email, self.password)  # Đăng nhập vào tài khoản email
                server.send_message(msg)  # Gửi email
            print("Email đã được gửi thành công!")
        except smtplib.SMTPAuthenticationError:
            print("Lỗi xác thực. Kiểm tra lại email và mật khẩu.")
        except smtplib.SMTPServerDisconnected:
            print("Kết nối tới máy chủ SMTP bị đóng đột ngột.")
        except Exception as e:
            print(f"Không thể gửi email. Lỗi: {e}")
