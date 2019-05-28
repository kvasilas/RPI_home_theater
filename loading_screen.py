read_sensor_msg.showWithTimeout('dry', 'calibrate', "Calibrating Moisture Sensor ...")

class read_sensor_msg(QMessageBox):
    def __init__(self, *__args):
        QMessageBox.__init__(self)
        self.autoclose = False
        self.currentTime = 0
        self.state = ''
        self.type = ''
    def showEvent(self, QShowEvent):
        self.currentTime = 0
        if self.autoclose:
            self.startTimer(1000)
    def timerEvent(self, *args, **kwargs):

        if(self.type == 'calibrate'):
            if(self.state == 'dry'):
                Jig_GUI.open_air_cal_vals = read.calibrate_dry()
            else:
                Jig_GUI.sub_fail = False
                Jig_GUI.submerged_cal_vals = read.calibrate_wet()
                for k in submerged_cal_vals:
                    if Jig_GUI.submerged_cal_vals[k] > Jig_GUI.SUBMERGED_TEST_LIMIT:
                        Jig_GUI.sub_fail = True
        elif(self.type == 'adc'):
            spike.configure_adcs()
        elif(self.type == 'head'):
            if not prog.program_head():
                exit()
        else:
            detected_hand = mfg.check_hand(.3, Jig_GUI.open_air_cal_vals)
            if('6' in self.state and detected_hand == 6):
                Jig_GUI.pass_6 = True
            if('18' in self.state and detected_hand == 18):
                Jig_GUI.pass_18 = True
            if('36' in self.state and detected_hand == 36):
                Jig_GUI.pass_36 = True

        time.sleep(1)
        self.done(0)
    @staticmethod
    def showWithTimeout(state, type, message, icon=QMessageBox.Information, buttons=QMessageBox.Ok):
        w = read_sensor_msg()
        w.autoclose = True
        w.state = state
        w.type = type
        w.setText(message)
        w.setIcon(icon)
        w.setStandardButtons(buttons)
        w.exec_()
