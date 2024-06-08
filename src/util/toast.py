from PyQt6 import QtWidgets


def toastWarning(message):
    QtWidgets.QMessageBox.warning(None, "Thông báo", message)


def toastInfo(message):
    QtWidgets.QMessageBox.information(None, "Thông báo", message)


def toastYesNoQuestion(message):
    reply = QtWidgets.QMessageBox.question(
        None,
        "Message",
        message,
        QtWidgets.QMessageBox.StandardButton.Yes
        | QtWidgets.QMessageBox.StandardButton.No,
        QtWidgets.QMessageBox.StandardButton.No,
    )
    if reply == QtWidgets.QMessageBox.StandardButton.Yes:
        return True
    return False
