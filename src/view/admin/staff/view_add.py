import sys
import os

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
)
from PyQt6 import QtCore, QtGui, QtWidgets
from controller.staff_controller import StaffController
from src.model.staff import Staff


class Ui_AddStaff(object):

    def __init__(self):
        self.sex = None
        self.staffController = StaffController()

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
        self.emailLabel.setGeometry(QtCore.QRect(104, 300, 51, 20))
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
        self.email.setGeometry(QtCore.QRect(180, 290, 281, 31))
        self.email.setObjectName("email")
        self.add_btn = QtWidgets.QPushButton(parent=AddStaff)
        self.add_btn.setGeometry(QtCore.QRect(430, 350, 121, 31))
        self.add_btn.setStyleSheet(
            "font-size: 16px;    background-color: #198754;    color: #FFFFFF;     border-radius: 5px"
        )
        self.add_btn.setObjectName("add_btn")
        self.render_password = QtWidgets.QPushButton(parent=AddStaff)
        self.render_password.setGeometry(QtCore.QRect(610, 200, 93, 28))
        self.render_password.setStyleSheet(
            "font-size: 14px;    background-color: #ffc107;     border-radius: 5px"
        )
        self.render_password.setObjectName("render_password")

        self.groupBox = QtWidgets.QGroupBox(parent=AddStaff)
        self.groupBox.setGeometry(QtCore.QRect(190, 200, 271, 80))
        self.groupBox.setStyleSheet("font-size: 16px; border: none")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.nam = QtWidgets.QRadioButton(parent=self.groupBox)
        self.nam.setGeometry(QtCore.QRect(20, 30, 71, 20))
        self.nam.setObjectName("radioButton")
        self.nu = QtWidgets.QRadioButton(parent=self.groupBox)
        self.nu.setGeometry(QtCore.QRect(100, 30, 61, 20))
        self.nu.setObjectName("radioButton_2")
        self.emailLabel_2 = QtWidgets.QLabel(parent=AddStaff)
        self.emailLabel_2.setGeometry(QtCore.QRect(90, 230, 71, 20))
        self.emailLabel_2.setObjectName("emailLabel_2")

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
        self.nam.setText(_translate("AddStaff", "Nam"))
        self.nu.setText(_translate("AddStaff", "Nữ"))
        self.emailLabel_2.setText(_translate("AddStaff", "Giới tính"))

    def setEvents(self):
        self.render_password.mousePressEvent = self.randomPassword
        self.add_btn.mousePressEvent = self.addStaff
        self.nam.mousePressEvent = self.selectNam
        self.nu.mousePressEvent = self.selectNu

    def checkEmail(self, event):
        email = self.email.text()
        result = self.staffController.checkEmail(email)
        if result.success is False:
            QtWidgets.QMessageBox.warning(None, "Thông báo", result.message)
            return
        QtWidgets.QMessageBox.information(None, "Thông báo", "Email OK")

    def checkPassword(self, event):
        password = self.password.text()
        result = self.staffController.checkPassword(password)
        if result.success is False:
            QtWidgets.QMessageBox.warning(None, "Thông báo", result.message)
            return
        QtWidgets.QMessageBox.information(None, "Thông báo", "Mật khẩu OK")

    def randomPassword(self, event):
        newPassword = self.staffController.getNewPassword()
        self.password.setText(newPassword)

    def getRank(self):
        rank = self.staffController.convertRank(self.rank.currentText())
        if rank is None:
            raise ValueError("Quyền không hợp lệ")
        return rank

    def getInfo(self):
        try:

            _sex = self.sex
            if _sex is None:
                QtWidgets.QMessageBox.warning(None, "Thông báo", "Chọn giới tính")
                return

            _password = self.password.text()
            email = self.email.text()
            if self.staffController.checkEmail(email).success is False:
                QtWidgets.QMessageBox.warning(None, "Thông báo", "Kiểm tra email")
                return
            if self.staffController.checkPassword(_password).success is False:
                QtWidgets.QMessageBox.warning(None, "Thông báo", "Kiểm tra mật khẩu")
                return

            _password = self.staffController.convertHashPasswords(_password)
            name = self.ten_nv.text()
            sdt = self.sdt.text()
            rank = self.getRank()
            idnv = self.staffController.getNewId()

            staff = Staff(
                idnv=idnv,
                name=name,
                sdt=sdt,
                email=email,
                sex=_sex,
                rank=rank,
                blockAt=None,
                password=_password,
            )
            return staff
        except (Exception, ValueError) as e:
            QtWidgets.QMessageBox.warning(None, "Lỗi", e)
            return None

    def addStaff(self, event):
        staff = self.getInfo()
        if staff is None:
            return
        result = self.staffController.add(staff, self.password.text())
        if result.success is False:
            QtWidgets.QMessageBox.warning(None, "Lỗi", result.message)
            return
        QtWidgets.QMessageBox.information(None, "Thông báo", "Thêm thành công")
        self.password.setText("")

    def selectNam(self, event):
        self.sex = 1
        self.nam.setChecked(True)

    def selectNu(self, event):
        self.sex = 0
        self.nu.setChecked(True)


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    AddStaff = QtWidgets.QMainWindow()
    ui = Ui_AddStaff()
    ui.setupUi(AddStaff)
    AddStaff.show()
    sys.exit(app.exec())
