# Python3
#
# Home Theater (Firestick ish) application.
# Intended to run on linux
#
# Author: Kirk KC Vasilas
# Created: April 2019
#

#PYTHON MODULES
import webbrowser
import googlesearch
import sys
import time
import os


#Qt Modules
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

#CUSTOM MODULES
import searching as s
#import hdmi_switch as hdmi


#GLOBAL PARAMETERS
chrome_path = ''
pic_path = os.getcwd() + 'pics_for_pi/'

#OS initialization
CPU_type = 'windows'
#CPU_type = 'pi'
#CPU_type = 'pine'
#CPU_type = 'kodi'

#Path parameter initialization
if CPU_type == 'windows':
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    #pic_path = 'C:/Users/USER/Documents/coding/projects/RPI_home_theater/pics_for_pi/'
elif CPU_type == 'pine':
    chrome_path = '/usr/bin/firefox %s'
    #pic_path = '/home/kc/Documents/projects/RPI_home_theater/pics_for_pi/'
else:
    chrome_path = '/usr/bin/google-chrome %s'
    #pic_path = '/home/kc/Documents/projects/RPI_home_theater/pics_for_pi/'


class home_theater(QWidget):

    title = ''
    found_list = []

    def __init__(self):
        super().__init__()
        self.title = 'Home Theater'
        self.left = 100
        self.top = 100
        self.block_size = 300
        self.search_bar_height = 40
        self.search_bar_width = 300
        border = 15
        self.pos1 = border
        self.pos2 = border + self.pos1 + self.block_size
        self.pos3 = border + self.pos2 + self.block_size
        self.width = border + self.pos3 + self.block_size
        self.height = self.pos3 + self.search_bar_height + border

        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        #labels

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
        search_btn = QPushButton('Search', self)
        search_btn.setGeometry(self.pos2-self.search_bar_width/3, self.pos3, self.search_bar_width/3, self.search_bar_height)
        search_btn.clicked.connect(self.search_title)
        self.search_bar = QLineEdit(self)
        self.search_bar.setGeometry(self.pos2, self.pos3, self.search_bar_width, self.search_bar_height)
        self.search_bar.returnPressed.connect(search_btn.click)

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
        #hdmi.switch(2)
        #press enter 2x to return back, this way it shouldnt accidently happen
        input()
        input()
        #hdmi.switch(1)

    def launch_xbox(self):
        #hdmi.switch(3)
        input()
        input()
        #hdmi.switch(1)

    def search_title(self):
            home_theater.title = self.search_bar.text()
            #home_theater.found_list = s.search_title(home_theater.title) #put this in the class
            loading_screen.showWithTimeout('search', "Looking for " + home_theater.title + "...")
            #test arrays
            #home_theater.found_list = ['https://www.netflix.com/title/80018294', 'hulu',  'https://www.amazon.com/Marvels-Daredevil-Season-1/dp/B01D1YR0N6']
            #home_theater.found_list = ['https://www..com/title/80018294', '',  'https://www..com/Marvels-Daredevil-Season-1/dp/B01D1YR0N6']
            print(home_theater.found_list)
            self.dialog = results(self)
            self.dialog.show()

    def exit_prog(self):
        print("##########","# bye KC #", "##########", sep='\n')
        sys.exit()


class results(home_theater):
    def __init__(self, parent= home_theater):
        super(results, self).__init__()
        self.initUI()

    def initUI(self):
        btn_size = 100
        self.setGeometry(250, 400, 2*btn_size, btn_size)
        keys = ['netflix', 'amazon', 'hulu', 'crackle']
        buttons = []
        for i in range(len(home_theater.found_list)):
            for j in range(len(keys)):
                if keys[j] in home_theater.found_list[i]:
                    buttons.append(keys[j])
        self.setWindowTitle(home_theater.title)
        L1 = QLabel(self)
        L1.setText('Watch ' + home_theater.title + ' on:' )
        if(home_theater.found_list == []):
            b = QPushButton("Not found Exit?", self)
            b.clicked.connect(self.exit_prog)
        elif(len(home_theater.found_list) == 1):
            b0 = QPushButton(buttons[0], self)
            b0.setToolTip('Open ' + buttons[0] +'?' )
            b0.clicked.connect(self.load_b0)
            b0.move(0, 25)
        elif(len(home_theater.found_list) == 2):
            #opt 1
            b0 = QPushButton(buttons[0], self)
            b0.setToolTip('Open ' + buttons[0] +'?' )
            b0.clicked.connect(self.load_b0)
            b0.move(0, 25)
            #opt 2
            b1 = QPushButton(buttons[1], self)
            b1.setToolTip('Open ' + buttons[1] +'?' )
            b1.clicked.connect(self.load_b1)
            b1.move(btn_size, 25)
        elif(len(home_theater.found_list) == 3):
            #opt 1
            b0 = QPushButton(buttons[0], self)
            b0.setToolTip('Open ' + buttons[0] +'?' )
            b0.clicked.connect(self.load_b0)
            b0.move(0, 25)
            #opt 2
            b1 = QPushButton(buttons[1], self)
            b1.setToolTip('Open ' + buttons[1] +'?' )
            b1.clicked.connect(self.load_b1)
            b1.move(btn_size, 25)
            #opt 3
            b2 = QPushButton(buttons[2], self)
            b2.setToolTip('Open ' + buttons[2] +'?' )
            b2.clicked.connect(self.load_b2)
            b2.move(0, 25 + btn_size/2.5)
        elif(len(home_theater.found_list) == 4):
            #opt 1
            b0 = QPushButton(buttons[0], self)
            b0.setToolTip('Open ' + buttons[0] +'?' )
            b0.clicked.connect(self.load_b0)
            b0.move(0, 25)
            #opt 2
            b1 = QPushButton(buttons[1], self)
            b1.setToolTip('Open ' + buttons[1] +'?' )
            b1.clicked.connect(self.load_b1)
            b1.move(btn_size, 25)
            #opt 3
            b2 = QPushButton(buttons[2], self)
            b2.setToolTip('Open ' + buttons[2] +'?' )
            b2.clicked.connect(self.load_b2)
            b2.move(0, 25 + btn_size/2.5)
            #opt 4
            b3 = QPushButton(buttons[3], self)
            b3.setToolTip('Open ' + buttons[3] +'?' )
            b3.clicked.connect(self.load_b3)
            b3.move(btn_size, 25 + btn_size/2.5)

        self.show()

    def load_b0(self):
        webbrowser.get(chrome_path).open(home_theater.found_list[0])
    def load_b1(self):
        webbrowser.get(chrome_path).open(home_theater.found_list[1])
    def load_b2(self):
        webbrowser.get(chrome_path).open(home_theater.found_list[2])
    def load_b3(self):
        webbrowser.get(chrome_path).open(home_theater.found_list[3])
    def exit_prog(self):
        pass

class loading_screen(QMessageBox):
    def __init__(self, *__args):
        QMessageBox.__init__(self)
        self.autoclose = False
        self.currentTime = 0
        self.state = ''
    def showEvent(self, QShowEvent):
        self.currentTime = 0
        if self.autoclose:
            self.startTimer(1000)
    def timerEvent(self, *args, **kwargs):
        if(self.state == 'search'):
            home_theater.found_list = s.search_title(home_theater.title) #put this in the class
        time.sleep(1)
        self.done(0)
    @staticmethod
    def showWithTimeout(state, message, icon=QMessageBox.Information, buttons=QMessageBox.Ok):
        w = loading_screen()
        w.autoclose = True
        w.state = state
        w.setText(message)
        w.setIcon(icon)
        w.setStandardButtons(buttons)
        w.exec_()


if __name__ == '__main__':
    #establish serial communication via hdmi_switch.py
    #check for hdmi state and go to 1
    app = QApplication(sys.argv)
    ex = home_theater()
    sys.exit(app.exec_())
