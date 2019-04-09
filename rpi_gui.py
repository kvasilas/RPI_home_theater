#Python3
#Kirk Vasilas
#
#
#

import webbrowser
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtCore import pyqtSlot

#import hdmi_switch as hdmi

#global parameters
# Windows for development
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
# Linux
# chrome_path = '/usr/bin/google-chrome %s'

#picture address
#windows
pic_path = 'C:/Users/USER/Documents/coding/projects/pics_for_pi/'
#linux

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

        #labels
        #welcome to Greenport label on top.  Make it look nice
        #     or... all steve's pals

        #buttons
        #nflx = QPushButton('NETFLIX', self)
        nflx = QPushButton('', self)
        nflx.setToolTip('Open NETFLIX?')
        nflx.setGeometry(self.pos1, self.pos1, self.block_size, self.block_size)
        nflx.clicked.connect(self.launch_nflx)
        nflx.setIcon(QIcon(pic_path + 'n.png'))
        nflx.setIconSize(QSize(self.block_size*.75, self.block_size*.75))

        #amzn = QPushButton('AMAZON', self)
        amzn = QPushButton('', self)
        amzn.setToolTip('Open Amazon Prime Video?')
        amzn.setGeometry(self.pos2, self.pos1, self.block_size, self.block_size)
        amzn.setIcon(QIcon(pic_path + 'prime.png'))
        amzn.setIconSize(QSize(self.block_size*.75, self.block_size*.75))
        amzn.clicked.connect(self.launch_amzn)

        #ytbe = QPushButton('YOUTUBE', self)
        ytbe = QPushButton('', self)
        ytbe.setToolTip('Open Youtube?')
        ytbe.setGeometry(self.pos3, self.pos1, self.block_size, self.block_size)
        ytbe.setIcon(QIcon(pic_path + 'youtube.png'))
        ytbe.setIconSize(QSize(self.block_size*.75, self.block_size*.75))
        ytbe.clicked.connect(self.launch_ytbe)

        #nwii = QPushButton('Nintendo Wii', self)
        nwii = QPushButton('', self)
        nwii.setToolTip('Switch input and play some Wii?')
        nwii.setGeometry(self.pos1, self.pos2, self.block_size, self.block_size)
        nwii.setIcon(QIcon(pic_path + 'wii.png'))
        nwii.setIconSize(QSize(self.block_size*.75, self.block_size*.75))
        nwii.clicked.connect(self.launch_nwii)

        #xbox = QPushButton('XBOX', self)
        xbox = QPushButton('', self)
        xbox.setToolTip('Switch input and play some Xbox?')
        xbox.setGeometry(self.pos2, self.pos2, self.block_size, self.block_size)
        xbox.setIcon(QIcon(pic_path + 'xbox.png'))
        xbox.setIconSize(QSize(self.block_size*.75, self.block_size*.75))
        xbox.clicked.connect(self.launch_xbox)

        #pc = QPushButton('COMPUTER', self)
        pc = QPushButton('', self)
        pc.setToolTip('Exit to computer?')
        pc.setGeometry(self.pos3, self.pos2, self.block_size, self.block_size)
        pc.setIcon(QIcon(pic_path + 'rpi.png'))
        pc.setIconSize(QSize(self.block_size*.75, self.block_size*.75))
        pc.clicked.connect(self.exit_prog)

        #google search input box

        self.show()

    def launch_nflx(self):
        url = 'https://www.netflix.com/browse'
        webbrowser.get(chrome_path).open(url)

    def launch_amzn(self):
        url = 'https://www.amazon.com/Prime-Video/b?ie=UTF8&node=2676882011'
        webbrowser.get(chrome_path).open(url)

    def launch_ytbe(self):
        url = 'https://www.youtube.com/'
        webbrowser.get(chrome_path).open(url)

    def launch_nwii(self):
        #hdmi.switch_input(2)
        #press enter 2x to return back, this way it shouldnt accidently happen
        input()
        input()
        #hdmi.hdmi_switch(1)

    def launch_xbox(self):
        #hdmi.switch_input(3)
        input()
        input()
        #hdmi.hdmi_switch(1)

    def exit_prog(self):
        print("bye KC")
        sys.exit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = home_theater()
    sys.exit(app.exec_())
