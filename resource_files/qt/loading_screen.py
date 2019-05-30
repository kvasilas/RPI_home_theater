l#loading_screen.showWithTimeout('search', "Looking for " + home_theater.title + "...")

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
