# Form implementation generated from reading ui file 'staff_working.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from src.model.staff_current import StaffCurrent
from src.view.staff.form_info import Ui_FormInfo


class Ui_StafWorking(object):
    def __init__(self, staffCurrent: StaffCurrent):
        self.staffCurrent = staffCurrent

    def setupUi(self, StafWorking):
        StafWorking.setObjectName("StafWorking")
        StafWorking.resize(881, 701)
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=StafWorking)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 361, 701))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.form = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.form.setContentsMargins(0, 0, 0, 0)
        self.form.setObjectName("form")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(parent=StafWorking)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(380, 0, 501, 701))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.chair_location = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.chair_location.setContentsMargins(0, 0, 0, 0)
        self.chair_location.setObjectName("chair_location")
        self.line = QtWidgets.QFrame(parent=StafWorking)
        self.line.setGeometry(QtCore.QRect(360, 30, 20, 651))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")

        self.retranslateUi(StafWorking)
        QtCore.QMetaObject.connectSlotsByName(StafWorking)

        self.showFormInfo()

    def showFormInfo(self):
        self.clearLayoutFormInfo()
        child_widget = QtWidgets.QWidget()
        child_ui = Ui_FormInfo(self.staffCurrent)
        child_ui.setupUi(child_widget)
        self.form.addWidget(child_widget)

    def clearLayoutFormInfo(self):
        while self.form.count():
            item = self.form.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()

    def retranslateUi(self, StafWorking):
        _translate = QtCore.QCoreApplication.translate
        StafWorking.setWindowTitle(_translate("StafWorking", "Staff Working"))
