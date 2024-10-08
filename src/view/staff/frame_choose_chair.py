# Form implementation generated from reading ui file 'frame_choose_chair.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_ChooseChair(QtWidgets.QMainWindow):
    def __init__(self, frameInfo, listIdSelected: list):
        self.frameInfo = frameInfo
        self.listIdSelected = listIdSelected
        super(Ui_ChooseChair, self).__init__()
        self.setupUi(self)
        self.setChair()
        self.selecting = []

    def setupUi(self, ChooseChair):
        ChooseChair.setObjectName("ChooseChair")
        ChooseChair.resize(501, 701)
        ChooseChair.setStyleSheet("font-size: 15px")
        self.pushButton = QtWidgets.QPushButton(parent=ChooseChair)
        self.pushButton.setGeometry(QtCore.QRect(90, 0, 321, 28))
        self.pushButton.setStyleSheet("border: 1px solid black;border-top: none; ")
        self.pushButton.setObjectName("pushButton")
        self.groupBox = QtWidgets.QGroupBox(parent=ChooseChair)
        self.groupBox.setGeometry(QtCore.QRect(30, 110, 441, 491))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayoutWidget = QtWidgets.QWidget(parent=self.groupBox)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 421, 471))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.box_chair = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.box_chair.setContentsMargins(0, 0, 0, 0)
        self.box_chair.setObjectName("box_chair")

        self.retranslateUi(ChooseChair)
        QtCore.QMetaObject.connectSlotsByName(ChooseChair)

    def retranslateUi(self, ChooseChair):
        _translate = QtCore.QCoreApplication.translate
        ChooseChair.setWindowTitle(_translate("ChooseChair", "Choose Chair"))
        self.pushButton.setText(_translate("ChooseChair", "Màn hình"))

        self.setChair()

    def setChair(self):
        self.buttons = {}
        chairs = [
            ["A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "A9", "A10"],
            ["B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8", "B9", "B10"],
            ["C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9", "C10"],
            ["D1", "D2", "D3", "D4", "D5", "D6", "D7", "D8", "D9", "D10"],
            ["E1", "E2", "E3", "E4", "E5", "E6", "E7", "E8", "E9", "E10"],
            ["F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9", "F10"],
            ["G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8", "G9", "G10"],
            ["H1", "H2", "H3", "H4", "H5", "H6", "H7", "H8", "H9", "H10"],
        ]

        for i, row in enumerate(chairs):
            for j, idChair in enumerate(row):
                btn = QtWidgets.QPushButton(idChair)
                btn.setFixedSize(QtCore.QSize(40, 40))
                btn.clicked.connect(self.on_click)
                self.box_chair.addWidget(btn, i, j)
                self.buttons[idChair] = btn
                if idChair in self.listIdSelected:
                    btn.setStyleSheet(
                        "margin: 3px; background-color: #dc3545;  border-radius: 3px; color: black"
                    )
                else:
                    btn.setStyleSheet(
                        "margin: 3px; background-color: #20c997;  border-radius: 3px; color: white"
                    )

    def on_click(self):
        button = self.sender()  # Lấy nút đã phát ra tín hiệu
        idChair = button.text()
        if idChair in self.listIdSelected:
            return
        elif idChair in self.selecting:
            index = self.selecting.index(idChair)
            self.selecting.pop(index)
            button.setStyleSheet(
                "margin: 3px; background-color: #20c997;  border-radius: 3px; color: white"
            )
        else:
            self.selecting.append(idChair)
            self.selecting.sort()
            button.setStyleSheet(
                "margin: 3px; background-color: #3d8bfd;  border-radius: 3px; color: black"
            )

        self.frameInfo.setSelectedIdChair(self.selecting)
