from PyQt6 import QtWidgets


def toastWarning(message):
    QtWidgets.QMessageBox.warning(None, "Thông báo", message)


def toastInfo(message):
    QtWidgets.QMessageBox.information(None, "Thông báo", message)
