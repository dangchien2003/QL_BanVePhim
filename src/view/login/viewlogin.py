from PyQt6 import QtCore, QtGui, QtWidgets
import sys
import os

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
)
from src.model.login.login import Login
from src.controller.login.login_controller import LoginController


class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(405, 309)
        Login.setAutoFillBackground(False)
        Login.setStyleSheet(
            "QLineEdit {\n"
            "    border-radius: 10px;\n"
            "    padding: 5px 10px;\n"
            "    font-size: 12px\n"
            "}\n"
            ""
        )
        self.label = QtWidgets.QLabel(parent=Login)
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
        self.label_2 = QtWidgets.QLabel(parent=Login)
        self.label_2.setGeometry(QtCore.QRect(80, 100, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=Login)
        self.label_3.setGeometry(QtCore.QRect(60, 140, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(parent=Login)
        self.lineEdit.setGeometry(QtCore.QRect(130, 90, 221, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=Login)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 140, 221, 31))
        self.lineEdit_2.setStyleSheet("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.pushButton = QtWidgets.QPushButton(parent=Login)
        self.pushButton.setGeometry(QtCore.QRect(40, 220, 151, 28))
        self.pushButton.setStyleSheet(
            "QPushButton:hover{\n" "    color: green\n" "}\n" "\n" ""
        )
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=Login)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 220, 161, 28))
        self.pushButton_2.setStyleSheet(
            "QPushButton:hover{\n" "    color: green\n" "}\n" ""
        )
        self.pushButton_2.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhNone)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_4 = QtWidgets.QLabel(parent=Login)
        self.label_4.setGeometry(QtCore.QRect(130, 180, 221, 16))
        self.label_4.setStyleSheet("color: red")
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

        # sự kiện
        # click
        self.pushButton.mousePressEvent = self.loginWidthAdmin
        self.pushButton_2.mousePressEvent = self.loginWidthStaff

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Ticket Manager"))
        self.label.setText(_translate("Login", "Đăng nhập"))
        self.label_2.setText(_translate("Login", "Email"))
        self.label_3.setText(_translate("Login", "Mật khẩu"))
        self.pushButton.setText(_translate("Login", "Đăng nhập với admin"))
        self.pushButton_2.setText(_translate("Login", "Đăng nhập với nhân viên"))

    def loginWidthAdmin(self, event):
        email = self.lineEdit.text()
        password = self.lineEdit_2.text()
        login = Login(email, password)
        loginController = LoginController(login)
        response = loginController.loginByAdmin()
        if response.success is False:
            self.label_4.setText(response.message)
            return
        self.label_4.setText("")

    def loginWidthStaff(self, event):
        email = self.lineEdit.text()
        password = self.lineEdit_2.text()
        login = Login(email, password)
        loginController = LoginController(login)
        response = loginController.loginByStaff()
        if response.success is False:
            self.label_4.setText(response.message)
            return
        self.label_4.setText("")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    login = QtWidgets.QWidget()
    ui = Ui_Login()
    ui.setupUi(login)
    login.show()
    sys.exit(app.exec())
