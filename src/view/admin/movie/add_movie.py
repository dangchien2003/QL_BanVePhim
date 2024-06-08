# Form implementation generated from reading ui file 'add_movie.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.
import sys
import os

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
)

from PyQt6 import QtCore, QtGui, QtWidgets
from src.model.movie import Movie
from src.controller.movie_controller import MovieController
from src.util.response import Res
from src.util import toast


class Ui_addMovie(object):

    def __init__(self) -> None:
        self.listMovies: list[Movie] = []
        self.movieController = MovieController()

    def setupUi(self, addMovie):
        addMovie.setObjectName("addMovie")
        addMovie.resize(1003, 666)
        addMovie.setStyleSheet(
            "QPushButton{border-radius: 10px; background: white; font-size: 15px} QSpinBox, QLineEdit{border-radius: 10px; padding: 5px 10px; font-size: 14px} QSpinBox{} QLabel{font-size: 14px} QRadioButton{font-size: 15px}"
        )
        self.centralwidget = QtWidgets.QWidget(parent=addMovie)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(addMovie)
        self.label.setGeometry(QtCore.QRect(120, 30, 221, 41))
        self.label.setStyleSheet('font: 20pt "Sitka"; font-weight: bold')
        self.label.setObjectName("label")
        self.add_all = QtWidgets.QPushButton(addMovie)
        self.add_all.setGeometry(QtCore.QRect(520, 270, 111, 28))
        self.add_all.setStyleSheet("background: #4dd4ac")
        self.add_all.setObjectName("add_all")
        self.remove = QtWidgets.QPushButton(addMovie)
        self.remove.setGeometry(QtCore.QRect(520, 330, 111, 28))
        self.remove.setStyleSheet("background-color: #ffda6a")
        self.remove.setObjectName("remove")
        self.remove_all = QtWidgets.QPushButton(addMovie)
        self.remove_all.setGeometry(QtCore.QRect(520, 390, 111, 28))
        self.remove_all.setStyleSheet("background-color: #dc3545")
        self.remove_all.setObjectName("remove_all")
        self.line = QtWidgets.QFrame(addMovie)
        self.line.setGeometry(QtCore.QRect(630, 40, 31, 621))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.add_table = QtWidgets.QPushButton(addMovie)
        self.add_table.setGeometry(QtCore.QRect(690, 350, 111, 28))
        self.add_table.setStyleSheet("background: #4dd4ac")
        self.add_table.setObjectName("add_table")
        self.clear_input = QtWidgets.QPushButton(addMovie)
        self.clear_input.setGeometry(QtCore.QRect(840, 350, 111, 28))
        self.clear_input.setStyleSheet("background: #ffda6a")
        self.clear_input.setObjectName("clear_input")
        self.price = QtWidgets.QSpinBox(addMovie)
        self.price.setGeometry(QtCore.QRect(790, 210, 150, 31))
        self.price.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        self.price.setCorrectionMode(
            QtWidgets.QAbstractSpinBox.CorrectionMode.CorrectToPreviousValue
        )
        self.price.setMaximum(1000000)
        self.price.setObjectName("price")
        self.time = QtWidgets.QSpinBox(addMovie)
        self.time.setGeometry(QtCore.QRect(790, 280, 150, 31))
        self.time.setStyleSheet("text-align: center")
        self.time.setMaximum(1000)
        self.time.setObjectName("time")
        self.time.setValue(0)
        self.tNPhimLabel = QtWidgets.QLabel(addMovie)
        self.tNPhimLabel.setGeometry(QtCore.QRect(663, 113, 61, 20))
        self.tNPhimLabel.setObjectName("tNPhimLabel")
        self.giThPNhTLabel = QtWidgets.QLabel(addMovie)
        self.giThPNhTLabel.setGeometry(QtCore.QRect(663, 220, 111, 20))
        self.giThPNhTLabel.setObjectName("giThPNhTLabel")
        self.name_movie = QtWidgets.QLineEdit(addMovie)
        self.name_movie.setGeometry(QtCore.QRect(741, 102, 241, 31))
        self.name_movie.setObjectName("name_movie")
        self.tuILabel = QtWidgets.QLabel(addMovie)
        self.tuILabel.setGeometry(QtCore.QRect(670, 170, 51, 21))
        self.tuILabel.setObjectName("tuILabel")
        self.thILNgLabel = QtWidgets.QLabel(addMovie)
        self.thILNgLabel.setGeometry(QtCore.QRect(663, 290, 111, 18))
        self.thILNgLabel.setObjectName("thILNgLabel")
        self.groupBox = QtWidgets.QGroupBox(addMovie)
        self.groupBox.setGeometry(QtCore.QRect(740, 150, 241, 51))
        self.groupBox.setStyleSheet("border: none")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.adult = QtWidgets.QRadioButton(parent=self.groupBox)
        self.adult.setGeometry(QtCore.QRect(180, 20, 51, 20))
        self.adult.setObjectName("adult")
        self.child = QtWidgets.QRadioButton(parent=self.groupBox)
        self.child.setGeometry(QtCore.QRect(5, 20, 81, 20))
        self.child.setObjectName("child")
        self.middle = QtWidgets.QRadioButton(parent=self.groupBox)
        self.middle.setGeometry(QtCore.QRect(100, 20, 51, 20))
        self.middle.setObjectName("middle")
        self.table = QtWidgets.QTableWidget(addMovie)
        self.table.setGeometry(QtCore.QRect(0, 90, 511, 571))
        self.table.setObjectName("table")
        self.table.setColumnCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(3, item)
        self.table.horizontalHeader().setStretchLastSection(True)

        self.retranslateUi(addMovie)
        QtCore.QMetaObject.connectSlotsByName(addMovie)

    def retranslateUi(self, addMovie):
        _translate = QtCore.QCoreApplication.translate
        addMovie.setWindowTitle(_translate("addMovie", "MainWindow"))
        self.label.setText(_translate("addMovie", "Phim đang thêm"))
        self.add_all.setText(_translate("addMovie", "Thêm tất cả"))
        self.remove.setText(_translate("addMovie", "Xoá"))
        self.remove_all.setText(_translate("addMovie", "Xoá tất cả"))
        self.add_table.setText(_translate("addMovie", "Thêm"))
        self.clear_input.setText(_translate("addMovie", "Dọn dẹp"))
        self.tNPhimLabel.setText(_translate("addMovie", "Tên phim"))
        self.giThPNhTLabel.setText(_translate("addMovie", "Giá thấp nhất(đ)"))
        self.tuILabel.setText(_translate("addMovie", "Độ tuổi"))
        self.thILNgLabel.setText(_translate("addMovie", "Thời lượng(phút)"))
        self.adult.setText(_translate("addMovie", "18+"))
        self.child.setText(_translate("addMovie", "Trẻ em"))
        self.middle.setText(_translate("addMovie", "16+"))
        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("addMovie", "Tên phim"))
        item = self.table.horizontalHeaderItem(1)
        item.setText(_translate("addMovie", "Độ tuổi"))
        item = self.table.horizontalHeaderItem(2)
        item.setText(_translate("addMovie", "Giá vé"))
        item = self.table.horizontalHeaderItem(3)
        item.setText(_translate("addMovie", "Thời lượng"))

        # event
        self.setEvent()
        self.setDefaultSelectTable()

    def setEvent(self):
        self.add_all.mousePressEvent = self.addAllMovie
        self.remove.mousePressEvent = self.removeMovie
        self.remove_all.mousePressEvent = self.removeAllMovie
        self.add_table.mousePressEvent = self.addMovieInTable
        self.clear_input.mousePressEvent = self.clearDataInput

        # Connect the cellClicked signal to the method
        self.table.cellClicked.connect(self.setSelectCurrent)

    def addAllMovie(self, event):
        print("addAllMovie")
        return

    def removeMovie(self, event):
        print("removeMovie")
        self.setDefaultSelectTable()

        return

    def removeAllMovie(self, event):
        print("removeAllMovie")
        self.setDefaultSelectTable()
        return

    def addMovieInTable(self, event):
        movie: Movie = self.getInfoMoviesForm()
        resultCheck: Res = self.movieController.checkInfoMovie(movie)
        if resultCheck.success is False:
            toast.toastWarning(resultCheck.message)
            return

        toast.toastInfo("Thêm thành công")

        self.listMovies.append(movie)

        resultConvert: Res = self.movieController.convertDataTable(self.listMovies)

        self.setDefaultSelectTable()
        self.pushMovieInTable(resultConvert.data)
        return

    def clearDataInput(self, event):
        return

    def setSelectCurrent(self, row, column):
        self.selectCurrent = row

    def setDefaultSelectTable(self):
        self.selectCurrent = None
        self.table.clearSelection()

    def getAgeChecked(self):
        if self.child.isChecked() is True:
            return 1
        elif self.middle.isChecked() is True:
            return 2
        elif self.adult.isChecked() is True:
            return 3
        return 0

    def pushMovieInTable(self, data: tuple):
        print(data)
        self.table.setRowCount(len(data))
        for row_num, row_data in enumerate(data):
            for col_num, col_data in enumerate(row_data):
                print(col_data)
                self.table.setItem(
                    row_num, col_num, QtWidgets.QTableWidgetItem(str(col_data))
                )

    def getInfoMoviesForm(self):
        name = self.name_movie.text()
        _age = self.getAgeChecked()
        price = self.price.text()
        _time = self.time.text()
        movie: Movie = Movie(name, _age, price, _time)
        return movie


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    addMovie = QtWidgets.QMainWindow()
    ui = Ui_addMovie()
    ui.setupUi(addMovie)
    addMovie.show()
    sys.exit(app.exec())