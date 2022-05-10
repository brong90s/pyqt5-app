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
  win.show()
  sys.exit(app.exec_())

window()