from PyQt6 import QtCore, QtGui, QtWidgets
import sys
import os

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
)
from src.model.login import Login
from src.controller.login_controller import LoginController
from src.view.admin.main_admin import MainAdmin


class Ui_Login(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setObjectName("self")
        self.setWindowIcon(
            QtGui.QIcon(
                os.path.join(
                    os.path.abspath(
                        os.path.join(os.path.dirname(__file__), "..", "..", "..")
                    ),
                    "public/logo.png",
                )
            )
        )
        self.resize(405, 309)
        self.setAutoFillBackground(False)
        self.setStyleSheet(
            "QLineEdit {\n"
            "    border-radius: 10px;\n"
            "    padding: 5px 10px;\n"
            "    font-size: 12px\n"
            "}\n"
            ""
        )
        self.label = QtWidgets.QLabel(parent=self)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(140, 30, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("font-size: 20px;\n" "font-weight: bold")
        self.label.setProperty("center", True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self)
        self.label_2.setGeometry(QtCore.QRect(80, 100, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self)
        self.label_3.setGeometry(QtCore.QRect(60, 140, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(parent=self)
        self.lineEdit.setGeometry(QtCore.QRect(130, 90, 221, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 140, 221, 31))
        self.lineEdit_2.setStyleSheet("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.pushButton = QtWidgets.QPushButton(parent=self)
        self.pushButton.setGeometry(QtCore.QRect(130, 220, 151, 28))
        self.pushButton.setStyleSheet(
            "QPushButton:hover{\n" "    color: green\n" "}\n" "\n" ""
        )
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(parent=self)
        self.label_4.setGeometry(QtCore.QRect(130, 180, 221, 16))
        self.label_4.setStyleSheet("color: red")
        self.label_4.setObjectName("label_4")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        # sự kiện
        self.setEvents()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Login", "Ticket Manager"))
        self.label.setText(_translate("Login", "Đăng nhập"))
        self.label_2.setText(_translate("Login", "Email"))
        self.label_3.setText(_translate("Login", "Mật khẩu"))
        self.pushButton.setText(_translate("Login", "Đăng nhập với admin"))
        self.lineEdit.setText("admin@gmail.com")
        self.lineEdit_2.setText("staff")

    def setEvents(self):
        # click
        self.pushButton.mousePressEvent = self.loginWidthAdmin

    def loginWidthAdmin(self, event):
        email = self.lineEdit.text()
        password = self.lineEdit_2.text()
        login = Login(email, password)
        loginController = LoginController(login)
        response = loginController.loginByAdmin()
        if response.success is False:
            self.label_4.setText(response.message)
            return
        self.mainWin = MainAdmin()

        # hiện main
        self.mainWin.show()

        # xoá đăng nhập
        self.deleteLater()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    login = Ui_Login()
    login.show()
    sys.exit(app.exec())
