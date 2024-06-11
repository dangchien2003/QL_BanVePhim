import sys
import os

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
)

from PyQt6 import QtCore, QtGui, QtWidgets

from src.model.movie import Movie
from src.controller.movie_controller import MovieController
from src.util import toast, number, time


class Ui_info_movie(object):
    def __init__(self) -> None:
        self.current_show = "all"
        self.dataTable = []
        self.selectCurrent = None
        self.movieController = MovieController()

    def setupUi(self, info_movie):
        info_movie.setObjectName("info_movie")
        info_movie.resize(998, 671)
        info_movie.setStyleSheet(
            "QPushButton{border-radius: 10px; background: white; font-size: 15px} QSpinBox, QLineEdit{border-radius: 10px; padding: 5px 10px; font-size: 14px} QSpinBox{} QLabel{font-size: 14px} QCheckBox, QRadioButton{font-size: 15px}"
        )

        self.label = QtWidgets.QLabel(parent=info_movie)
        self.label.setGeometry(QtCore.QRect(30, 30, 55, 16))
        self.label.setObjectName("label")
        self.find_id = QtWidgets.QLineEdit(parent=info_movie)
        self.find_id.setGeometry(QtCore.QRect(100, 20, 191, 31))
        self.find_id.setObjectName("find_id")
        self.find_name = QtWidgets.QLineEdit(parent=info_movie)
        self.find_name.setGeometry(QtCore.QRect(100, 70, 231, 31))
        self.find_name.setObjectName("find_name")
        self.label_2 = QtWidgets.QLabel(parent=info_movie)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 71, 16))
        self.label_2.setObjectName("label_2")
        self.table = QtWidgets.QTableWidget(parent=info_movie)
        self.table.setGeometry(QtCore.QRect(0, 150, 621, 498))
        self.table.viewport().setProperty(
            "cursor", QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor)
        )
        self.table.setObjectName("table")
        self.table.setColumnCount(7)
        self.table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(6, item)
        self.table.horizontalHeader().setSortIndicatorShown(False)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.tNPhimLabel_2 = QtWidgets.QLabel(parent=info_movie)
        self.tNPhimLabel_2.setGeometry(QtCore.QRect(662, 170, 61, 20))
        self.tNPhimLabel_2.setObjectName("tNPhimLabel_2")
        self.time = QtWidgets.QSpinBox(parent=info_movie)
        self.time.setGeometry(QtCore.QRect(789, 337, 151, 31))
        self.time.setStyleSheet("text-align: center")
        self.time.setMaximum(1000)
        self.time.setObjectName("time")
        self.edit = QtWidgets.QPushButton(parent=info_movie)
        self.edit.setGeometry(QtCore.QRect(689, 500, 111, 28))
        self.edit.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.edit.setStyleSheet("background: #4dd4ac")
        self.edit.setObjectName("edit")
        self.groupBox_2 = QtWidgets.QGroupBox(parent=info_movie)
        self.groupBox_2.setGeometry(QtCore.QRect(739, 207, 251, 51))
        self.groupBox_2.setStyleSheet("border: none")
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.adult = QtWidgets.QRadioButton(parent=self.groupBox_2)
        self.adult.setGeometry(QtCore.QRect(190, 20, 51, 20))
        self.adult.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.adult.setObjectName("adult")
        # empty
        self.age_Empty = QtWidgets.QRadioButton(parent=self.groupBox_2)
        self.age_Empty.setGeometry(QtCore.QRect(190, 20, 51, 20))
        self.age_Empty.setCursor(
            QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor)
        )
        self.age_Empty.setObjectName("age_Empty")
        self.age_Empty.setVisible(False)

        self.child = QtWidgets.QRadioButton(parent=self.groupBox_2)
        self.child.setGeometry(QtCore.QRect(10, 20, 81, 20))
        self.child.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.child.setObjectName("child")
        self.middle = QtWidgets.QRadioButton(parent=self.groupBox_2)
        self.middle.setGeometry(QtCore.QRect(110, 20, 51, 20))
        self.middle.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.middle.setObjectName("middle")
        self.thILNgLabel_2 = QtWidgets.QLabel(parent=info_movie)
        self.thILNgLabel_2.setGeometry(QtCore.QRect(662, 347, 111, 18))
        self.thILNgLabel_2.setObjectName("thILNgLabel_2")
        self.line_2 = QtWidgets.QFrame(parent=info_movie)
        self.line_2.setGeometry(QtCore.QRect(629, 27, 31, 621))
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.tuILabel_2 = QtWidgets.QLabel(parent=info_movie)
        self.tuILabel_2.setGeometry(QtCore.QRect(669, 227, 51, 21))
        self.tuILabel_2.setObjectName("tuILabel_2")
        self.price = QtWidgets.QSpinBox(parent=info_movie)
        self.price.setGeometry(QtCore.QRect(789, 267, 151, 31))
        self.price.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        self.price.setCorrectionMode(
            QtWidgets.QAbstractSpinBox.CorrectionMode.CorrectToPreviousValue
        )
        self.price.setMaximum(1000000)
        self.price.setObjectName("price")
        self.giThPNhTLabel_2 = QtWidgets.QLabel(parent=info_movie)
        self.giThPNhTLabel_2.setGeometry(QtCore.QRect(662, 277, 111, 20))
        self.giThPNhTLabel_2.setObjectName("giThPNhTLabel_2")
        self.hide = QtWidgets.QPushButton(parent=info_movie)
        self.hide.setGeometry(QtCore.QRect(839, 500, 111, 28))
        self.hide.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.hide.setStyleSheet("background: #ffda6a")
        self.hide.setObjectName("hide")
        self.name_movie = QtWidgets.QLineEdit(parent=info_movie)
        self.name_movie.setGeometry(QtCore.QRect(740, 159, 241, 31))
        self.name_movie.setObjectName("name_movie")
        self.tuILabel_3 = QtWidgets.QLabel(parent=info_movie)
        self.tuILabel_3.setGeometry(QtCore.QRect(690, 400, 81, 21))
        self.tuILabel_3.setObjectName("tuILabel_3")
        self.find_hide = QtWidgets.QPushButton(parent=info_movie)
        self.find_hide.setGeometry(QtCore.QRect(510, 110, 111, 28))
        self.find_hide.setCursor(
            QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor)
        )
        self.find_hide.setStyleSheet("background: #e35d6a")
        self.find_hide.setObjectName("find_hide")
        self.find_ok = QtWidgets.QPushButton(parent=info_movie)
        self.find_ok.setGeometry(QtCore.QRect(360, 110, 131, 28))
        self.find_ok.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.find_ok.setStyleSheet("background:  #4dd4ac")
        self.find_ok.setObjectName("find_ok")
        self.find = QtWidgets.QPushButton(parent=info_movie)
        self.find.setGeometry(QtCore.QRect(100, 110, 131, 28))
        self.find.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.find.setStyleSheet("background: #6ea8fe")
        self.find.setObjectName("find")
        self.tNPhimLabel_3 = QtWidgets.QLabel(parent=info_movie)
        self.tNPhimLabel_3.setGeometry(QtCore.QRect(662, 111, 61, 20))
        self.tNPhimLabel_3.setObjectName("tNPhimLabel_3")
        self.idMovie = QtWidgets.QLineEdit(parent=info_movie)
        self.idMovie.setGeometry(QtCore.QRect(740, 100, 241, 31))
        self.idMovie.setReadOnly(True)
        self.idMovie.setObjectName("idMovie")
        self.tuILabel_4 = QtWidgets.QLabel(parent=info_movie)
        self.tuILabel_4.setGeometry(QtCore.QRect(680, 450, 81, 21))
        self.tuILabel_4.setObjectName("tuILabel_4")
        self.createAt = QtWidgets.QLabel(parent=info_movie)
        self.createAt.setGeometry(QtCore.QRect(790, 450, 151, 21))
        self.createAt.setText("")
        self.createAt.setObjectName("createAt")
        self.hide_status = QtWidgets.QCheckBox(parent=info_movie)
        self.hide_status.setEnabled(False)
        self.hide_status.setGeometry(QtCore.QRect(790, 400, 160, 20))
        self.hide_status.setStyleSheet("margin-left: 2px")
        self.hide_status.setText("")
        self.hide_status.setObjectName("hide_status")

        self.retranslateUi(info_movie)
        QtCore.QMetaObject.connectSlotsByName(info_movie)

    def retranslateUi(self, info_movie):
        _translate = QtCore.QCoreApplication.translate
        info_movie.setWindowTitle(_translate("info_movie", "MainWindow"))
        self.label.setText(_translate("info_movie", "Mã phim"))
        self.label_2.setText(_translate("info_movie", "Tên phim"))
        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("info_movie", "Mã phim"))
        item = self.table.horizontalHeaderItem(1)
        item.setText(_translate("info_movie", "Tên phim"))
        item = self.table.horizontalHeaderItem(2)
        item.setText(_translate("info_movie", "Độ tuổi"))
        item = self.table.horizontalHeaderItem(3)
        item.setText(_translate("info_movie", "Giá vé"))
        item = self.table.horizontalHeaderItem(4)
        item.setText(_translate("info_movie", "Thời lượng"))
        item = self.table.horizontalHeaderItem(5)
        item.setText(_translate("info_movie", "Trạng thái"))
        item = self.table.horizontalHeaderItem(6)
        item.setText(_translate("info_movie", "Tạo lúc"))
        self.tNPhimLabel_2.setText(_translate("info_movie", "Tên phim"))
        self.edit.setText(_translate("info_movie", "Sửa"))
        self.adult.setText(_translate("info_movie", "18+"))
        self.child.setText(_translate("info_movie", "Trẻ em"))
        self.middle.setText(_translate("info_movie", "16+"))
        self.thILNgLabel_2.setText(_translate("info_movie", "Thời lượng(phút)"))
        self.tuILabel_2.setText(_translate("info_movie", "Độ tuổi"))
        self.giThPNhTLabel_2.setText(_translate("info_movie", "Giá thấp nhất(đ)"))
        self.hide.setText(_translate("info_movie", "Dừng chiếu"))
        self.tuILabel_3.setText(_translate("info_movie", "Dừng chiếu"))
        self.find_hide.setText(_translate("info_movie", "Đã dừng"))
        self.find_ok.setText(_translate("info_movie", "Đang phát hành"))
        self.find.setText(_translate("info_movie", "Tìm kiếm"))
        self.tNPhimLabel_3.setText(_translate("info_movie", "Mã phim"))
        self.tuILabel_4.setText(_translate("info_movie", "Thời gian tạo"))
        self.setSizeTable()
        self.setEvents()
        self.showAllMovie()

    def setEvents(self):
        self.find.mousePressEvent = self.clickFind
        self.find_ok.mousePressEvent = self.clickShowDataOK
        self.find_hide.mousePressEvent = self.clickShowDataHided
        self.edit.mousePressEvent = self.clickUpdateNewData
        self.hide.mousePressEvent = self.clickUpdateHideMovie
        self.table.cellClicked.connect(self.tableClick)

    def setSizeTable(self):
        self.table.setColumnWidth(0, 160)
        self.table.setColumnWidth(6, 140)

    def setDefaultTable(self):
        self.table.clearSelection()
        self.selectCurrent = None

    def clickFind(self, event):
        id = self.find_id.text()
        name = self.find_name.text()
        result = self.movieController.findMovie(id, name)
        if result.success is False:
            toast.toastWarning(result.message)
            return
        self.setDefaultTable()
        self.dataTable = result.data
        dataTable = self.convertFetchDataToDataTable(result.data)
        self.showDataToTable(dataTable)
        self.focus("find")
        self.current_show = "find"

    def clickShowDataOK(self, event):
        if self.current_show == "ok":
            return
        self.showAllMovieOk()
        return

    def clickShowDataHided(self, event):
        if self.current_show == "hide":
            return
        self.showAllMovieHided()
        return

    def clickUpdateNewData(self, event):
        if self.selectCurrent is None:
            toast.toastWarning("Chọn lại phim")
            return
        name = self.name_movie.text()
        age = self.getAgeChecked()
        price = self.price.value()
        time = self.time.value()
        movie = Movie(name=name, age=age, minPrice=price, time=time)
        checkMovie = self.movieController.checkInfoMovie(movie)
        if checkMovie.success is False:
            toast.toastWarning(checkMovie.message)
            return

        id = self.idMovie.text()

        if toast.toastYesNoQuestion(f"Yes để tiếp tục thay đổi {id}") is False:
            return

        movie.setId(id)

        updateInfoMovie = self.movieController.updateMovie(movie)
        if updateInfoMovie.success is False:
            toast.toastWarning(updateInfoMovie.message)
            return

        toast.toastInfo(f"Cập nhật thành công {movie.id}")

        # update list data
        row = self.table.currentRow()
        newMovie = self.getNewData(movie, self.dataTable[row])
        self.dataTable[row] = newMovie
        self.showDataToTable(self.convertFetchDataToDataTable(self.dataTable))
        return

    def getNewData(self, newMovie: Movie, oldMovie: tuple) -> tuple:
        newDataList = list(oldMovie)
        newDataList[1] = newMovie.name
        newDataList[2] = int(newMovie.age)
        newDataList[3] = int(newMovie.minPrice)
        newDataList[4] = int(newMovie.time)
        return tuple(newDataList)

    def clickUpdateHideMovie(self, event):
        id = self.idMovie.text()
        getMovie = self.movieController.getOneMovieById(id)
        if getMovie.success is False:
            toast.toastWarning(getMovie.message)
            return

        movie = list(getMovie.data)
        if movie[5] is not None:
            toast.toastInfo("Phim đã được dừng trước đó")
            return

        if toast.toastYesNoQuestion("Sẽ không thể mở lại sau khi dừng") is False:
            return

        hided = self.movieController.setHideMovie(id)

        if hided.success is False:
            toast.toastWarning(hided.message)
            return

        toast.toastInfo(f"{id} đã bị dừng chiếu")
        timeString = time.convertTimeStampToString(hided.data)
        self.hide_status.setChecked(True)
        self.hide_status.setText(timeString)
        selectCurrent = self.table.currentRow()
        self.table.setItem(selectCurrent, 5, QtWidgets.QTableWidgetItem("Hide"))
        return

    def tableClick(self, row, col):
        data = self.dataTable[row]
        self.selectCurrent = row
        self.showDataToForm(data)
        return

    def showAllMovieOk(self):
        result = self.movieController.allMovieOk()
        if result.success is False:
            toast.toastWarning(result.message)
            return
        self.setDefaultTable()
        self.dataTable = result.data
        dataTable = self.convertFetchDataToDataTable(result.data)
        self.showDataToTable(dataTable)
        self.focus("ok")
        self.current_show = "ok"

    def showAllMovieHided(self):
        result = self.movieController.allMovieHided()
        if result.success is False:
            toast.toastWarning(result.message)
            return
        self.setDefaultTable()
        self.dataTable = result.data
        dataTable = self.convertFetchDataToDataTable(result.data)
        self.showDataToTable(dataTable)
        self.focus("hide")
        self.current_show = "hide"

    def showAllMovie(self):
        result = self.movieController.allMovie()
        if result.success is False:
            toast.toastWarning(result.message)
            return
        self.setDefaultTable()
        self.dataTable = result.data
        dataTable = self.convertFetchDataToDataTable(result.data)
        self.showDataToTable(dataTable)
        self.focus("all")
        self.current_show = "all"

    def focus(self, item=("ok", "hide")):
        if item == "ok":
            self.find_ok.setStyleSheet("background: #4dd4ac; color: white")
            self.find_hide.setStyleSheet("background: #e35d6a; color: black")
        elif item == "hide":
            self.find_ok.setStyleSheet("background: #4dd4ac; color: black")
            self.find_hide.setStyleSheet("background: #e35d6a; color: white")
        else:
            self.find_ok.setStyleSheet("background: #4dd4ac; color: black")
            self.find_hide.setStyleSheet("background: #e35d6a; color: black")

    def showDataToTable(self, data):
        self.table.setRowCount(len(data))
        for row_num, row_data in enumerate(data):
            for col_num, col_data in enumerate(row_data):
                self.table.setItem(
                    row_num, col_num, QtWidgets.QTableWidgetItem(str(col_data))
                )

    def convertFetchDataToDataTable(self, data: tuple):
        result = []
        for item in data:
            item_list = list(item)
            item_list[3] = f"{number.convertPrice(item_list[3])} đ"
            item_list[4] = f"{item_list[4]} phút"
            item_list[5] = "OK" if item_list[5] is None else "Hide"
            item_list[6] = time.convertTimeStampToString(item_list[6])
            result.append(tuple(item_list))
        return result

    def showDataToForm(self, data):
        self.clearForm()
        listData = list(data)
        self.idMovie.setText(listData[0])
        self.name_movie.setText(listData[1])
        self.checkedAge(listData[2])
        self.price.setValue(listData[3])
        self.time.setValue(listData[4])
        if listData[5] is not None:
            self.hide_status.setChecked(True)
            self.hide_status.setText(time.convertTimeStampToString(listData[5]))

        self.createAt.setText(time.convertTimeStampToString(listData[6]))

    def checkedAge(self, age):
        if age < 16:
            self.child.setChecked(True)
        elif age < 18:
            self.middle.setChecked(True)
        else:
            self.adult.setChecked(True)

    def clearForm(self):
        self.idMovie.setText("")
        self.name_movie.setText("")
        self.age_Empty.setChecked(True)
        self.price.setValue(0)
        self.time.setValue(0)
        self.hide_status.setChecked(False)
        self.hide_status.setText("")
        self.createAt.setText("")

    def getAgeChecked(self):
        if self.child.isChecked() is True:
            return 1
        elif self.middle.isChecked() is True:
            return 2
        elif self.adult.isChecked() is True:
            return 3
        return 0


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    info_movie = QtWidgets.QMainWindow()
    ui = Ui_info_movie()
    ui.setupUi(info_movie)
    info_movie.show()
    sys.exit(app.exec())
