import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon


def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(600, 200, 500, 500)
    win.setWindowTitle("Restricted")
    win.setWindowIcon(QIcon("Sanity.png"))
    win.setToolTip("Restricted")

    lbl_name = QtWidgets.QLabel(win)
    lbl_name.setText("Enter name : ")
    lbl_name.move(50, 50)

    lbl_surename = QtWidgets.QLabel(win)
    lbl_surename.setText("Enter surname : ")
    lbl_surename.move(50, 90)

    txt_name = QtWidgets.QLineEdit(win)
    txt_name.move(200, 50)

    txt_surname = QtWidgets.QLineEdit(win)
    txt_surname.move(200, 90)

    def clicked(self):
        print('button clicked')
        print('name :' + txt_name.text())
        print('surname :' + txt_surname.text())

    btn_save = QtWidgets.QPushButton(win)
    btn_save.setText('Save')
    btn_save.clicked.connect(clicked)
    btn_save.move(200, 130)

    win.show()
    sys.exit(app.exec_())


window()
