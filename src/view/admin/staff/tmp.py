import sys
import os

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
)
from PyQt6 import QtCore, QtGui, QtWidgets
from src.controller.staff.add_controller import AddStaffController
from src.model.staff import Staff


class Ui_AddStaff(object):
    def __init__(self):
        self.addController = AddStaffController()

    def setupUi(self, AddStaff):
        AddStaff.setObjectName("AddStaff")
        AddStaff.resize(1000, 670)
        AddStaff.setStyleSheet(
            "QLabel{font-size: 16px;}\n"
            "QLineEdit, QComboBox{padding: 5px 10px; border-radius: 10px; font-size: 14px}\n"
            "QMainWindow{background-color: #ececec}"
        )
        self.rank = QtWidgets.QComboBox(parent=AddStaff)
        self.rank.setGeometry(QtCore.QRect(606, 95, 221, 31))
        self.rank.setObjectName("rank")
        self.rank.addItem("")
        self.sTLabel = QtWidgets.QLabel(parent=AddStaff)
        self.sTLabel.setGeometry(QtCore.QRect(120, 170, 51, 20))
        self.sTLabel.setObjectName("sTLabel")
        self.quyNLabel = QtWidgets.QLabel(parent=AddStaff)
        self.quyNLabel.setGeometry(QtCore.QRect(530, 100, 61, 20))
        self.quyNLabel.setObjectName("quyNLabel")
        self.passwordLabel = QtWidgets.QLabel(parent=AddStaff)
        self.passwordLabel.setGeometry(QtCore.QRect(510, 170, 71, 20))
        self.passwordLabel.setObjectName("passwordLabel")
        self.lb_tennv = QtWidgets.QLabel(parent=AddStaff)
        self.lb_tennv.setGeometry(QtCore.QRect(50, 100, 111, 20))
        self.lb_tennv.setObjectName("lb_tennv")
        self.emailLabel = QtWidgets.QLabel(parent=AddStaff)
        self.emailLabel.setGeometry(QtCore.QRect(110, 240, 51, 20))
        self.emailLabel.setObjectName("emailLabel")
        self.ten_nv = QtWidgets.QLineEdit(parent=AddStaff)
        self.ten_nv.setGeometry(QtCore.QRect(186, 96, 281, 31))
        self.ten_nv.setText("")
        self.ten_nv.setObjectName("ten_nv")
        self.sdt = QtWidgets.QLineEdit(parent=AddStaff)
        self.sdt.setGeometry(QtCore.QRect(186, 163, 281, 31))
        self.sdt.setObjectName("sdt")
        self.password = QtWidgets.QLineEdit(parent=AddStaff)
        self.password.setGeometry(QtCore.QRect(608, 160, 221, 31))
        self.password.setObjectName("password")
        self.email = QtWidgets.QLineEdit(parent=AddStaff)
        self.email.setGeometry(QtCore.QRect(186, 230, 281, 31))
        self.email.setObjectName("email")
        self.add_btn = QtWidgets.QPushButton(parent=AddStaff)
        self.add_btn.setGeometry(QtCore.QRect(430, 350, 121, 31))
        self.add_btn.setStyleSheet(
            "font-size: 16px;    background-color: #198754;    color: #FFFFFF;     border-radius: 5px"
        )
        self.add_btn.setObjectName("add_btn")
        self.render_password = QtWidgets.QPushButton(parent=AddStaff)
        self.render_password.setGeometry(QtCore.QRect(710, 200, 111, 28))
        self.render_password.setStyleSheet(
            "font-size: 14px;    background-color: #ffc107;     border-radius: 5px"
        )
        self.render_password.setObjectName("render_password")
        self.check_password = QtWidgets.QPushButton(parent=AddStaff)
        self.check_password.setGeometry(QtCore.QRect(610, 200, 93, 28))
        self.check_password.setStyleSheet(
            "font-size: 14px;    background-color: #198754;        border-radius: 5px"
        )
        self.check_password.setObjectName("check_password")
        self.check_email = QtWidgets.QPushButton(parent=AddStaff)
        self.check_email.setGeometry(QtCore.QRect(190, 270, 93, 28))
        self.check_email.setStyleSheet(
            "font-size: 14px;    background-color: #198754;        border-radius: 5px"
        )
        self.check_email.setObjectName("check_email")

        self.retranslateUi(AddStaff)
        QtCore.QMetaObject.connectSlotsByName(AddStaff)

        # event
        self.setEvents()

    def retranslateUi(self, AddStaff):
        _translate = QtCore.QCoreApplication.translate
        AddStaff.setWindowTitle(_translate("AddStaff", "MainWindow"))
        self.rank.setItemText(0, _translate("AddStaff", "Staff"))
        self.sTLabel.setText(_translate("AddStaff", "SĐT"))
        self.quyNLabel.setText(_translate("AddStaff", "Quyền"))
        self.passwordLabel.setText(_translate("AddStaff", "Password"))
        self.lb_tennv.setText(_translate("AddStaff", "Tên nhân viên"))
        self.emailLabel.setText(_translate("AddStaff", "Email"))
        self.add_btn.setText(_translate("AddStaff", "Thêm"))
        self.render_password.setText(_translate("AddStaff", "Lấy mật khẩu"))
        self.check_password.setText(_translate("AddStaff", "Kiểm tra"))
        self.check_email.setText(_translate("AddStaff", "Kiểm tra"))

    def setEvents(self):
        self.check_email.mousePressEvent = self.checkEmail
        self.check_password.mousePressEvent = self.checkPassword
        self.render_password.mousePressEvent = self.randomPassword
        self.add_btn.mousePressEvent = self.addStaff

    def checkEmail(self, event):
        email = self.email.text()
        result = self.addController.checkEmail(email)
        if result.success is False:
            QtWidgets.QMessageBox.warning(None, "Thông báo", result.message)
            return
        QtWidgets.QMessageBox.information(None, "Thông báo", "Email OK")

    def checkPassword(self, event):
        password = self.password.text()
        result = self.addController.checkPassword(password)
        if result.success is False:
            QtWidgets.QMessageBox.warning(None, "Thông báo", result.message)
            return
        QtWidgets.QMessageBox.information(None, "Thông báo", "Mật khẩu OK")

    def randomPassword(self, event):
        newPassword = self.addController.getNewPassword()
        self.password.setText(newPassword)

    def addStaff(self, event):
        name = self.ten_nv.text()
        sdt = self.sdt.text()
        email = self.email.text()
        rank = self.rank.currentIndex()
        password = self.password.text()
        idnv = self.addController.getNewId()
        staff = Staff(
            idnv=idnv,
            name=name,
            sdt=sdt,
            email=email,
            rank=rank,
            password=password,
        )


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    AddStaff = QtWidgets.QMainWindow()
    ui = Ui_AddStaff()
    ui.setupUi(AddStaff)
    AddStaff.show()
    sys.exit(app.exec())
