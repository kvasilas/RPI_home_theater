#Python3
#Kirk Vasilas
#
#
#

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class home_theater(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Welcome to Greenport'
        self.left = 100
        self.top = 100
        self.block_size = 300
        border = 15
        self.pos1 = border
        self.pos2 = border + self.pos1 + self.block_size
        self.pos3 = border + self.pos2 + self.block_size
        self.width = border + self.pos3 + self.block_size
        self.height = self.pos3

        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        #buttons
        nflx = QPushButton('NETFLIX', self)
        nflx.setToolTip('Open NETFLIX?')
        nflx.setGeometry(self.pos1, self.pos1, self.block_size, self.block_size)
        nflx.clicked.connect(self.launch_nflx)

        amzn = QPushButton('AMAZON', self)
        amzn.setToolTip('Open Amazon Prime Video?')
        amzn.setGeometry(self.pos2, self.pos1, self.block_size, self.block_size)
        amzn.clicked.connect(self.launch_amzn)

        ytbe = QPushButton('YOUTUBE', self)
        ytbe.setToolTip('Open Youtube?')
        ytbe.setGeometry(self.pos3, self.pos1, self.block_size, self.block_size)
        ytbe.clicked.connect(self.launch_ytbe)

        snos = QPushButton('SONOS', self)
        snos.setToolTip('Open Sonos music player?')
        snos.setGeometry(self.pos1, self.pos2, self.block_size, self.block_size)
        snos.clicked.connect(self.launch_snos)

        othr = QPushButton('XBOX', self)
        othr.setToolTip('Switch input and play some Xbox?')
        othr.setGeometry(self.pos2, self.pos2, self.block_size, self.block_size)
        othr.clicked.connect(self.launch_othr)

        pc = QPushButton('COMPUTER', self)
        pc.setToolTip('Exit to computer?')
        pc.setGeometry(self.pos3, self.pos2, self.block_size, self.block_size)
        pc.clicked.connect(self.exit_prog)

        self.show()

    def launch_nflx(self):
        pass

    def launch_amzn(self):
        pass

    def launch_ytbe(self):
        pass

    def launch_snos(self):
        pass

    def launch_othr(self):
        pass

    def exit_prog(self):
        sys.exit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = home_theater()
    sys.exit(app.exec_())
