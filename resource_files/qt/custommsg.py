        read_sensor_msg.showWithTimeout('wet',"Calibrating Moisture Sensor", icon=QMessageBox.Warning)

#also look up progress bar



class read_sensor_msg(QMessageBox):

    def __init__(self, *__args):
        QMessageBox.__init__(self)
        self.autoclose = False
        self.currentTime = 0
        self.state = 'dry'

    def showEvent(self, QShowEvent):
        self.currentTime = 0
        print('hello')
        if self.autoclose:
            self.startTimer(1000)

    def timerEvent(self, *args, **kwargs):
        if(self.state == 'wet'):
            print("submerged")
        else:
            print("open air")
        time.sleep(3)
        print(100)
        App.word = "vanilla"
        self.done(0)

    @staticmethod

    def showWithTimeout(state, message, icon=QMessageBox.Information, buttons=QMessageBox.Ok):
        w = read_sensor_msg()
        w.autoclose = True
        w.state = state
        w.setText(message)
        w.setIcon(icon)
        w.setStandardButtons(buttons)
        w.exec_()
