def launch_title(self):
    webbrowser.get(chrome_path).open(self.found_list[0])

def search_title(self):
    title = self.search_bar.text()
    print(title)
    self.found_list = s.search_title(title)
    print(self.found_list)
    msg = QMessageBox()
    msg.setText(title)
    msg.setInformativeText("has been found at the following:")
    msg.setWindowTitle("Where to Watch")
    if(len(self.found_list)==4):
        pass
        #b1 = QPushButton(found_list[0], self)
        #QMessageBox with all 4 buttons
        #search the string from www.xxxx.com pill the # XXX
    elif(len(self.found_list)==3):
        pass
        #same
    elif(len(self.found_list)==2):
        b1 = msg.addButton(QPushButton('Amazon'), QMessageBox.YesRole)
        b2 = msg.addButton(QPushButton('crackle'), QMessageBox.YesRole)
        if msg.clickedButton() == b1:
            #msg.buttonClicked.connect(self.launch_title)
            webbrowser.get(chrome_path).open(self.found_list[0])
        else:
            webbrowser.get(chrome_path).open(self.found_list[1])
            #msg.buttonClicked.connect(self.launch_ytbe) #currently sends both
        #same
    elif(len(self.found_list)==1):
        pass
    else:
        pass
        #QMessageBox show not found sorry :(
    retval = msg.exec_()
    #if passed make small buttons on a QMessageBox to pick which to load it on
    #use url to pass that adress to google and load it
    #then quit the QMessageBox
    #maybe make new widget? becuase this doesnt have the functionality
