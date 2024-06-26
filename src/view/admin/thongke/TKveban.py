# Form implementation generated from reading ui file 'TKveban.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from src.util import toast
from src.controller.Tkveban_controller import TKveban_controller


class Ui_TKveban(object):
    def __init__(self):
        self.tkVeBan_Controler = TKveban_controller()
        self.selected = 0

    def setupUi(self, TKveban):
        TKveban.setObjectName("TKveban")
        TKveban.resize(1000, 679)
        self.centralwidget = QtWidgets.QWidget(parent=TKveban)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(parent=self.centralwidget)
        self.line.setGeometry(QtCore.QRect(400, 0, 20, 641))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 20, 191, 61))
        self.label.setStyleSheet(
            'font: 18pt "MS Shell Dlg 2";\n' "color:rgb(92, 95, 255);"
        )
        self.label.setObjectName("label")
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(460, 10, 151, 101))
        self.widget.setObjectName("widget")
        self.label_4 = QtWidgets.QLabel(parent=self.widget)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 111, 91))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("public/tickets.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(440, 120, 501, 351))
        self.tableWidget.setStyleSheet("")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.horizontalHeader().setSectionResizeMode(
            QtWidgets.QHeaderView.ResizeMode.Stretch
        )
        self.groupBox_theothoigian = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_theothoigian.setGeometry(QtCore.QRect(40, 120, 321, 351))
        self.groupBox_theothoigian.setStyleSheet(
            "\n"
            'font: 11pt "MS Shell Dlg 2";\n'
            " border-radius: 25px;\n"
            "  border: 2px solid #73AD21;"
        )
        self.groupBox_theothoigian.setObjectName("groupBox_theothoigian")
        self.button_ngay = QtWidgets.QRadioButton(parent=self.groupBox_theothoigian)
        self.button_ngay.setGeometry(QtCore.QRect(30, 40, 121, 31))
        self.button_ngay.setStyleSheet(
            'font: 12pt "MS Shell Dlg 2";\n' "border: white;"
        )
        self.button_ngay.setObjectName("button_ngay")
        self.button_thang = QtWidgets.QRadioButton(parent=self.groupBox_theothoigian)
        self.button_thang.setGeometry(QtCore.QRect(30, 120, 121, 41))
        self.button_thang.setStyleSheet(
            'font: 12pt "MS Shell Dlg 2";\n' "border: white;"
        )
        self.button_thang.setObjectName("button_thang")
        self.button_nam = QtWidgets.QRadioButton(parent=self.groupBox_theothoigian)
        self.button_nam.setGeometry(QtCore.QRect(30, 220, 101, 31))
        self.button_nam.setStyleSheet('font: 12pt "MS Shell Dlg 2";\n' "border: white;")
        self.button_nam.setObjectName("button_nam")
        self.box_ngay = QtWidgets.QSpinBox(parent=self.groupBox_theothoigian)
        self.box_ngay.setGeometry(QtCore.QRect(50, 80, 101, 31))
        self.box_ngay.setMinimumSize(QtCore.QSize(101, 31))
        self.box_ngay.setMaximumSize(QtCore.QSize(101, 31))
        self.box_ngay.setStyleSheet("border:707070;")
        self.box_ngay.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.box_ngay.setMinimum(1)
        self.box_ngay.setMaximum(31)
        self.box_ngay.setObjectName("box_ngay")
        self.box_thang = QtWidgets.QSpinBox(parent=self.groupBox_theothoigian)
        self.box_thang.setGeometry(QtCore.QRect(50, 170, 101, 31))
        self.box_thang.setMinimumSize(QtCore.QSize(101, 31))
        self.box_thang.setMaximumSize(QtCore.QSize(101, 31))
        self.box_thang.setStyleSheet("border:707070;")
        self.box_thang.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.box_thang.setMinimum(1)
        self.box_thang.setMaximum(12)
        self.box_thang.setObjectName("box_thang")
        self.box_nam = QtWidgets.QSpinBox(parent=self.groupBox_theothoigian)
        self.box_nam.setGeometry(QtCore.QRect(50, 260, 101, 31))
        self.box_nam.setMinimumSize(QtCore.QSize(101, 31))
        self.box_nam.setMaximumSize(QtCore.QSize(101, 31))
        self.box_nam.setStyleSheet("border:707070;")
        self.box_nam.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.box_nam.setMinimum(2018)
        self.box_nam.setMaximum(2024)
        self.box_nam.setObjectName("box_nam")
        self.button_timkiem = QtWidgets.QPushButton(parent=self.groupBox_theothoigian)
        self.button_timkiem.setGeometry(QtCore.QRect(180, 290, 81, 41))
        self.button_timkiem.setStyleSheet(
            'font: 10pt "MS Shell Dlg 2";\n'
            "border: 3px solid white ; /* Đường viền đen dày 2px */\n"
            "border-radius: 15px;\n"
            "background-color:#27ae60;\n"
            " color: #ffffff;"
        )
        self.button_timkiem.setObjectName("button_timkiem")

        self.retranslateUi(TKveban)
        QtCore.QMetaObject.connectSlotsByName(TKveban)

    def retranslateUi(self, TKveban):
        _translate = QtCore.QCoreApplication.translate
        TKveban.setWindowTitle(_translate("TKveban", "MainWindow"))
        self.label.setText(_translate("TKveban", "Bộ lọc thống kê"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("TKveban", "Thời gian"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("TKveban", "Tổng vé"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("TKveban", "Doanh thu"))
        self.groupBox_theothoigian.setTitle(_translate("TKveban", "Theo thời gian"))
        self.button_ngay.setText(_translate("TKveban", "Theo ngày"))
        self.button_thang.setText(_translate("TKveban", "Theo tháng"))
        self.button_nam.setText(_translate("TKveban", "Theo năm"))
        self.button_timkiem.setText(_translate("TKveban", "Tìm kiếm"))
        self.setEvents()

    def getSelected(self):
        if self.button_ngay.isChecked():
            self.selected = 1
        elif self.button_thang.isChecked():
            self.selected = 2
        elif self.button_nam.isChecked():
            self.selected = 3

    def setEvents(self):
        self.button_timkiem.mousePressEvent = self.getData

    def getData(self, event):
        self.getSelected()
        result = self.tkVeBan_Controler.getData(
            self.selected,
            self.box_ngay.value(),
            self.box_thang.value(),
            self.box_nam.value(),
        )
        if result.success == False:
            toast.toastWarning(result.message)
            return
        self.putdata(result.data)

    def putdata(self, data: list[object]):
        self.tableWidget.setRowCount(len(data))
        for row_idx, row_data in enumerate(data):
            self.tableWidget.setItem(
                row_idx, 0, QtWidgets.QTableWidgetItem(str(row_data["date"]))
            )
            self.tableWidget.setItem(
                row_idx, 1, QtWidgets.QTableWidgetItem(str(row_data["soVe"]))
            )
            self.tableWidget.setItem(
                row_idx, 2, QtWidgets.QTableWidgetItem(str(row_data["doanhThu"]))
            )


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    TKveban = QtWidgets.QMainWindow()
    ui = Ui_TKveban()
    ui.setupUi(TKveban)
    TKveban.show()
    sys.exit(app.exec())
