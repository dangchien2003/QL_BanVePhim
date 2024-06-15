import os
from PyQt6 import QtCore, QtWidgets, QtGui


class Ui_SelectCalendar(object):
    def __init__(self, parent, date=None, format=None):
        self.parent = parent
        self.date = date
        self.format = format

    def setupUi(self, SelectCalendar):
        SelectCalendar.setObjectName("SelectCalendar")
        SelectCalendar.setWindowIcon(
            QtGui.QIcon(
                os.path.join(
                    os.path.abspath(
                        os.path.join(os.path.dirname(__file__), "..", "..", "..")
                    ),
                    "public/logo.png",
                )
            )
        )
        SelectCalendar.resize(404, 254)
        self.calendar = QtWidgets.QCalendarWidget(parent=SelectCalendar)
        self.calendar.setGeometry(QtCore.QRect(0, 0, 401, 251))
        self.calendar.setLocale(
            QtCore.QLocale(
                QtCore.QLocale.Language.Vietnamese, QtCore.QLocale.Country.Vietnam
            )
        )
        self.calendar.setObjectName("calendar")
        self.wait = QtWidgets.QPushButton(parent=SelectCalendar)
        self.wait.setGeometry(QtCore.QRect(40, 110, 331, 41))
        self.wait.setStyleSheet(
            "font-size: 16px; background-color: rgba(224, 255, 84, 0.8); border-radius: 10px"
        )
        self.wait.setObjectName("wait")
        self.wait.setVisible(False)

        self.retranslateUi(SelectCalendar)
        QtCore.QMetaObject.connectSlotsByName(SelectCalendar)

    def retranslateUi(self, SelectCalendar):
        _translate = QtCore.QCoreApplication.translate
        SelectCalendar.setWindowTitle(_translate("SelectCalendar", "Select Calendar"))
        self.wait.setText(_translate("SelectCalendar", "Chờ một chút..."))

        self.setDefaultCalendar()
        self.setSelectDate()
        self.setEvent()

    def setSelectDate(self):
        if self.date is None:
            return
        date = QtCore.QDate.fromString(self.date, self.format)
        self.calendar.setSelectedDate(date)

    def setDefaultCalendar(self):
        self.calendar.setMinimumDate(QtCore.QDate.currentDate().addDays(-1))

    def setEvent(self):
        self.calendar.selectionChanged.connect(self.clickChangeTime)

    def clickChangeTime(self):
        selected = self.calendar.selectedDate().toString("dd-MM-yyyy")
        self.parent.changeValueSelectDay(selected)
