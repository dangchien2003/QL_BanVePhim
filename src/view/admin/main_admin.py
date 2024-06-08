import sys
import os

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
)
from PyQt6 import QtCore, QtGui, QtWidgets
from src.view.admin.staff.view_add import Ui_AddStaff
from src.view.admin.staff.info import Ui_info
from src.view.admin.movie.add_movie import Ui_addMovie


class MainAdmin(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setObjectName("self")
        self.resize(1001, 700)
        self.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(parent=self)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1001, 671))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.view = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.view.setContentsMargins(0, 0, 0, 0)
        self.view.setObjectName("view")
        self.hello_btn = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.hello_btn.setStyleSheet(
            "height: 100px;    font-size: 30px;    background-color: transparent;"
        )
        self.hello_btn.setObjectName("hello_btn")
        self.view.addWidget(self.hello_btn)
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1001, 26))
        self.menubar.setObjectName("menubar")
        self.menubar.setStyleSheet(
            """ 
            QMenuBar {
                border-bottom: 1px solid #dee2e6; 
                border-radius: 8px;
            }
            
            QMenuBar::item:selected {
                background: #ced4da;
            }
            """
        )
        self.menuQu_n_l_nh_n_vi_n = QtWidgets.QMenu(parent=self.menubar)
        self.menuQu_n_l_nh_n_vi_n.setObjectName("menuQu_n_l_nh_n_vi_n")
        self.menuQu_n_l_phim = QtWidgets.QMenu(parent=self.menubar)
        self.menuQu_n_l_phim.setObjectName("menuQu_n_l_phim")
        self.menuL_ch_chi_u = QtWidgets.QMenu(parent=self.menubar)
        self.menuL_ch_chi_u.setObjectName("menuL_ch_chi_u")
        self.menuTh_ng_k = QtWidgets.QMenu(parent=self.menubar)
        self.menuTh_ng_k.setObjectName("menuTh_ng_k")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.add_staff = QtGui.QAction(parent=self)
        self.add_staff.setObjectName("add_staff")
        self.all_staff = QtGui.QAction(parent=self)
        self.all_staff.setObjectName("all_staff")
        self.all_movie = QtGui.QAction(parent=self)
        self.all_movie.setObjectName("all_movie")
        self.add_movie = QtGui.QAction(parent=self)
        self.add_movie.setObjectName("add_movie")
        self.add_calendar = QtGui.QAction(parent=self)
        self.add_calendar.setObjectName("add_calendar")
        self.all_calendar = QtGui.QAction(parent=self)
        self.all_calendar.setObjectName("all_calendar")
        self.ticket_statistical = QtGui.QAction(parent=self)
        self.ticket_statistical.setObjectName("ticket_statistical")
        self.revenue_statistical = QtGui.QAction(parent=self)
        self.revenue_statistical.setObjectName("revenue_statistical")
        self.menuQu_n_l_nh_n_vi_n.addAction(self.all_staff)
        self.menuQu_n_l_nh_n_vi_n.addSeparator()
        self.menuQu_n_l_nh_n_vi_n.addAction(self.add_staff)
        self.menuQu_n_l_phim.addAction(self.all_movie)
        self.menuQu_n_l_phim.addSeparator()
        self.menuQu_n_l_phim.addAction(self.add_movie)
        self.menuL_ch_chi_u.addAction(self.all_calendar)
        self.menuL_ch_chi_u.addSeparator()
        self.menuL_ch_chi_u.addAction(self.add_calendar)
        self.menuTh_ng_k.addAction(self.ticket_statistical)
        self.menuTh_ng_k.addSeparator()
        self.menuTh_ng_k.addAction(self.revenue_statistical)
        self.menubar.addAction(self.menuQu_n_l_nh_n_vi_n.menuAction())
        self.menubar.addAction(self.menuQu_n_l_phim.menuAction())
        self.menubar.addAction(self.menuL_ch_chi_u.menuAction())
        self.menubar.addAction(self.menuTh_ng_k.menuAction())

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        # event
        self.setEvents()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "admin"))
        self.hello_btn.setText(_translate("MainWindow", "Xin chào"))
        self.menuQu_n_l_nh_n_vi_n.setTitle(_translate("MainWindow", "Nhân viên"))
        self.menuQu_n_l_phim.setTitle(_translate("MainWindow", "Phim"))
        self.menuL_ch_chi_u.setTitle(_translate("MainWindow", "Lịch chiếu"))
        self.menuTh_ng_k.setTitle(_translate("MainWindow", "Thống kê"))
        self.add_staff.setText(_translate("MainWindow", "Thêm nhân viên"))
        self.all_staff.setText(_translate("MainWindow", "Xem toàn bộ"))
        self.all_movie.setText(_translate("MainWindow", "Tất cả phim"))
        self.add_movie.setText(_translate("MainWindow", "Thêm phim"))
        self.add_calendar.setText(_translate("MainWindow", "Tạo lịch"))
        self.all_calendar.setText(_translate("MainWindow", "Tất cả lịch"))
        self.ticket_statistical.setText(_translate("MainWindow", "Vé phim"))
        self.revenue_statistical.setText(_translate("MainWindow", "Doanh thu"))

    def clearLayout(self):
        while self.view.count():
            item = self.view.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()

    def setEvents(self):
        self.all_staff.triggered.connect(self.showFrameAllStaff)
        self.add_staff.triggered.connect(self.showFrameAddStaff)
        self.add_movie.triggered.connect(self.showFrameAddMovie)

    def showFrameAllStaff(self):
        self.clearLayout()
        child_widget = QtWidgets.QWidget()
        child_ui = Ui_info()
        child_ui.setupUi(child_widget)
        self.view.addWidget(child_widget)

    def showFrameAddStaff(self):
        self.clearLayout()
        child_widget = QtWidgets.QWidget()
        child_ui = Ui_AddStaff()
        child_ui.setupUi(child_widget)
        self.view.addWidget(child_widget)

    def showFrameAddMovie(self):
        self.clearLayout()
        child_widget = QtWidgets.QWidget()
        child_ui = Ui_addMovie()
        child_ui.setupUi(child_widget)
        self.view.addWidget(child_widget)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainAdmin()
    mainWin.show()
    sys.exit(app.exec())
