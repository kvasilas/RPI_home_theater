#Python3
#Kirk Vasilas
#
#
#

import webbrowser
import googlesearch
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QLineEdit, QLabel
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtCore import pyqtSlot


class classA(QWidget):
    str = '123'
    def __init__(self, parent=None):
        super().__init__()
        self.initUI()


    def initUI(self):
        btn = QPushButton("click me", self)
        btn.clicked.connect(self.on_pushButton_clicked)

    def on_pushButton_clicked(self):
        classA.str = "sasasa"
        self.dialog = classB(self)
        self.dialog.show()


class classB(classA):
    def __init__(self, parent= classA):
        super(classB, self).__init__(parent)
        self.initUI()

    def initUI(self):
        pass
        print(classA.str)
        self.setWindowTitle(classA.str)

def main():
    app = QApplication(sys.argv)
    main = classA()
    main.show()
    sys.exit(app.exec_())


main()
