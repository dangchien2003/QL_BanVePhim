from PyQt6 import QtCore, QtGui, QtWidgets
import sys
import os

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
)
from src.model.login import Login
from src.model.staff_current import StaffCurrent
from src.controller.login_controller import LoginController
from src.view.staff.check_ticket import Ui_MainWindow


class Ui_FrameLogin(object):
    def setupUi(self, FrameLogin):
        FrameLogin.setObjectName("FrameLogin")
        FrameLogin.setWindowIcon(
            QtGui.QIcon(
                os.path.join(
                    os.path.abspath(
                        os.path.join(os.path.dirname(__file__), "..", "..", "..")
                    ),
                    "public/logo.png",
                )
            )
        )
        FrameLogin.resize(405, 276)
        FrameLogin.setAutoFillBackground(False)
        FrameLogin.setStyleSheet(
            "QLineEdit {\n"
            "    border-radius: 10px;\n"
            "    padding: 5px 10px;\n"
            "    font-size: 12px\n"
            "}\n"
            ""
        )
        self.label = QtWidgets.QLabel(parent=FrameLogin)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(140, 30, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(1)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("font-size: 20px;\n" "font-weight: bold")
        self.label.setProperty("center", True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=FrameLogin)
        self.label_2.setGeometry(QtCore.QRect(70, 100, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=FrameLogin)
        self.label_3.setGeometry(QtCore.QRect(40, 140, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.email = QtWidgets.QLineEdit(parent=FrameLogin)
        self.email.setGeometry(QtCore.QRect(130, 90, 221, 31))
        self.email.setObjectName("email")
        self.password = QtWidgets.QLineEdit(parent=FrameLogin)
        self.password.setGeometry(QtCore.QRect(130, 140, 221, 31))
        self.password.setStyleSheet("")
        self.password.setObjectName("password")
        self.password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.btn_login = QtWidgets.QPushButton(parent=FrameLogin)
        self.btn_login.setGeometry(QtCore.QRect(130, 210, 151, 28))
        self.btn_login.setStyleSheet(
            "QPushButton:hover{\n" "    color: green\n" "}\n" "\n" ""
        )
        self.btn_login.setObjectName("btn_login")
        self.label_4 = QtWidgets.QLabel(parent=FrameLogin)
        self.label_4.setGeometry(QtCore.QRect(130, 180, 221, 16))
        self.label_4.setStyleSheet("color: red")
        self.label_4.setObjectName("label_4")

        self.retranslateUi(FrameLogin)
        QtCore.QMetaObject.connectSlotsByName(FrameLogin)

    def retranslateUi(self, FrameLogin):
        _translate = QtCore.QCoreApplication.translate
        FrameLogin.setWindowTitle(_translate("FrameLogin", "Ticket Manager"))
        self.label.setText(_translate("FrameLogin", "Quầy soát vé"))
        self.label_2.setText(_translate("FrameLogin", "Email"))
        self.label_3.setText(_translate("FrameLogin", " Mật khẩu"))
        self.btn_login.setText(_translate("FrameLogin", "Đăng nhập"))

        # sự kiện
        self.setEvents()

    def setEvents(self):
        # click
        self.btn_login.mousePressEvent = self.loginWidthStaff

    def loginWidthStaff(self, event):
        email = self.email.text()
        password = self.password.text()
        login = Login(email, password)
        loginController = LoginController(login)
        response = loginController.loginByStaff()
        if response.success is False:
            self.label_4.setText(response.message)
            return
        self.label_4.setText("")
        staffCurrent = response.data
        self.showMain(staffCurrent)
        # xoá đăng nhập
        self.btn_login.parent().deleteLater()

    def showMain(self, staffCurrent: StaffCurrent):
        if not staffCurrent or staffCurrent.id is None:
            print("Không có id staff")
            return
        self.main = QtWidgets.QWidget()
        self.ui = Ui_MainWindow(staffCurrent)
        self.ui.setupUi(self.main)
        self.main.show()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    FrameLogin = QtWidgets.QWidget()
    ui = Ui_FrameLogin()
    ui.setupUi(FrameLogin)
    FrameLogin.show()
    sys.exit(app.exec())
