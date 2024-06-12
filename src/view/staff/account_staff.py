# Form implementation generated from reading ui file 'account_staff.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
import os

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
)
from PyQt6 import QtCore, QtGui, QtWidgets
from src.model.staff_current import StaffCurrent
from src.controller.staff_controller import StaffController
from src.util import toast


class Ui_accountStaff(object):
    def __init__(self, frameMain):
        self.frameMain = frameMain
        self.staffController = StaffController()
        self.staffCurrent: StaffCurrent = None

    def setupUi(self, accountStaff):
        accountStaff.setObjectName("accountStaff")
        accountStaff.resize(201, 701)
        accountStaff.setStyleSheet(
            "QLabel{font-size: 15px; } QPushButton, QLineEdit{border-radius: 10px; font-size: 15px; }"
        )
        self.groupLogin = QtWidgets.QGroupBox(parent=accountStaff)
        self.groupLogin.setEnabled(True)
        self.groupLogin.setGeometry(QtCore.QRect(0, 180, 201, 191))
        self.groupLogin.setStyleSheet(
            "QPushButton:hover{color: white;} QLineEdit{padding: 5px 10px} QGroupBox{border: none}"
        )
        self.groupLogin.setTitle("")
        self.groupLogin.setObjectName("groupLogin")
        self.label = QtWidgets.QLabel(parent=self.groupLogin)
        self.label.setGeometry(QtCore.QRect(10, 10, 81, 21))
        self.label.setObjectName("label")
        self.email = QtWidgets.QLineEdit(parent=self.groupLogin)
        self.email.setGeometry(QtCore.QRect(10, 40, 181, 31))
        self.email.setObjectName("email")
        self.label_2 = QtWidgets.QLabel(parent=self.groupLogin)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 81, 21))
        self.label_2.setObjectName("label_2")
        self.password = QtWidgets.QLineEdit(parent=self.groupLogin)
        self.password.setGeometry(QtCore.QRect(10, 110, 181, 31))
        self.password.setObjectName("password")
        self.btnLogin = QtWidgets.QPushButton(parent=self.groupLogin)
        self.btnLogin.setGeometry(QtCore.QRect(50, 150, 93, 28))
        self.btnLogin.setStyleSheet("background: #479f76")
        self.btnLogin.setObjectName("btnLogin")
        self.groupInfo = QtWidgets.QGroupBox(parent=accountStaff)
        self.groupInfo.setGeometry(QtCore.QRect(0, 220, 201, 111))
        self.groupInfo.setStyleSheet("font-size: 15px; border: none")
        self.groupInfo.setTitle("")
        self.groupInfo.setObjectName("groupInfo")
        self.label_3 = QtWidgets.QLabel(parent=self.groupInfo)
        self.label_3.setGeometry(QtCore.QRect(30, 20, 151, 21))
        self.label_3.setObjectName("label_3")
        self.nameStaff = QtWidgets.QPushButton(parent=self.groupInfo)
        self.nameStaff.setGeometry(QtCore.QRect(10, 50, 171, 28))
        self.nameStaff.setStyleSheet("background: none; font-size: 18px;")
        self.nameStaff.setText("")
        self.nameStaff.setObjectName("nameStaff")
        self.logout = QtWidgets.QLabel(parent=self.groupInfo)
        self.logout.setGeometry(QtCore.QRect(60, 90, 61, 16))
        self.logout.setStyleSheet(
            "font-size: 13px; color: #0a58ca; text-decoration: underline;"
        )
        self.logout.setObjectName("logout")

        self.retranslateUi(accountStaff)
        QtCore.QMetaObject.connectSlotsByName(accountStaff)

    def retranslateUi(self, accountStaff):
        _translate = QtCore.QCoreApplication.translate
        accountStaff.setWindowTitle(_translate("accountStaff", "Account Staff"))
        self.label.setText(_translate("accountStaff", "Email:"))
        self.label_2.setText(_translate("accountStaff", "Mật khẩu:"))
        self.btnLogin.setText(_translate("accountStaff", "Đăng nhập"))
        self.label_3.setText(_translate("accountStaff", "Đang đăng nhập với:"))
        self.logout.setText(_translate("accountStaff", "Đăng xuất"))
        self.setDefaultFrame()
        self.setEvent()
        self.setAnimation()

    def setAnimation(self):
        self.animationLoginSuccess()
        self.animationLogout()

    def animationLoginSuccess(self):
        # show
        # animation for group login
        effect = QtWidgets.QGraphicsOpacityEffect()
        self.groupInfo.setGraphicsEffect(effect)
        effect.setOpacity(1)

        # name animation
        increaseOpacity = QtCore.QPropertyAnimation(effect, b"opacity")

        # set properties animation
        increaseOpacity.setDuration(1000)
        increaseOpacity.setStartValue(0)
        increaseOpacity.setEndValue(1)

        # add animation in group
        self.showFormInfoEffect = QtCore.QSequentialAnimationGroup()
        self.showFormInfoEffect.addAnimation(increaseOpacity)
        self.showFormInfoEffect.setLoopCount(1)

    def animationLogout(self):
        # show
        effect = QtWidgets.QGraphicsOpacityEffect()
        self.groupLogin.setGraphicsEffect(effect)
        effect.setOpacity(1)
        increaseOpacity = QtCore.QPropertyAnimation(effect, b"opacity")
        increaseOpacity.setDuration(1000)
        increaseOpacity.setStartValue(0)
        increaseOpacity.setEndValue(1)

        # add animation in group
        self.showFormLoginEffect = QtCore.QSequentialAnimationGroup()
        self.showFormLoginEffect.addAnimation(increaseOpacity)
        self.showFormLoginEffect.setLoopCount(1)

    def setEvent(self):
        self.btnLogin.mousePressEvent = self.clickLogin
        self.logout.mousePressEvent = self.clickOut
        return

    def setDefaultFrame(self):
        self.email.setText("abc@gmail.com")
        self.password.setText("staff")
        self.groupInfo.setVisible(False)
        self.password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)

    def clickLogin(self, event):
        email = self.email.text()
        password = self.password.text()

        resultLogin = self.staffController.login(email, password)

        if resultLogin.success is False:
            toast.toastWarning(resultLogin.message)
            return

        self.staffCurrent = resultLogin.data
        self.clearFormLogin()
        self.showInfoAccount()
        self.frameMain.setStaffCurrent(self.staffCurrent)
        self.frameMain.showFrameWorking()

    def showInfoAccount(self):
        self.nameStaff.setText(self.staffCurrent.name)
        self.groupLogin.setVisible(False)
        self.groupInfo.setVisible(True)
        self.showFormInfoEffect.start()

    def clickOut(self, event):
        if toast.toastYesNoQuestion("Bạn đang đăng xuất") is False:
            return

        self.staffCurrent = None
        self.groupInfo.setVisible(False)
        self.groupLogin.setVisible(True)
        self.showFormLoginEffect.start()
        self.frameMain.showRequireLogin()

    def clearFormLogin(self):
        self.email.setText("")
        self.password.setText("")
