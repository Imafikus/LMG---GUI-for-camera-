import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import os



class CameraWindow(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 250, 350)
        self.setWindowTitle('Field of View')
        self.setFixedSize(self.size())

        self.values = open("config/camera.txt").read().splitlines()
        
        #FOV part
        self.lbl1 = QLabel("Width of View:", self)
        self.lbl1.move(20, 55)

        self.lbl2 = QLabel("Deg.", self)
        self.lbl2.move(140, 30)

        self.p1 = QLineEdit(self)
        self.p1.move(135, 50)
        self.p1.resize(45,30)
        self.p1.setText(self.values[0])
        
        #CVP part
        self.lbl3 = QLabel("Center of View:", self)
        self.lbl3.move(20, 120)

        self.lbl4 = QLabel("Az.", self)
        self.lbl4.move(140, 95)

        self.p2 = QLineEdit(self)
        self.p2.move(135, 115)
        self.p2.resize(45,30)
        self.p2.setText(self.values[1])

        
        self.lbl5 = QLabel("H.", self)
        self.lbl5.move(200, 95)

        self.p3 = QLineEdit(self)
        self.p3.move(190, 115)
        self.p3.resize(45,30)
        self.p3.setText(self.values[2])
        
        #ROT part
        self.lbl3 = QLabel("Camera Rotation:", self)
        self.lbl3.move(20, 185)


        self.lbl6 = QLabel("Deg.", self)
        self.lbl6.move(140, 160)

        self.p4 = QLineEdit(self)
        self.p4.move(135, 180)
        self.p4.resize(45,30)
        self.p4.setText(self.values[3])



                
        OK = QPushButton('OK', self)
        OK.resize(150, 50)
        OK.move(50, 250)
        OK.clicked.connect(self.okButton)
        
    def okButton(self):

        self.WoV = self.p1.text()
        self.Az = self.p2.text() 
        self.H = self.p3.text()
        self.Rot = self.p4.text()
        
        self.WoV_msg = ""
        if self.checkWoV() == False: self.WoV_msg = "Width of View must have a value between 0-180.\n"

        self.Az_msg = ""
        if self.checkAz() == False: self.Az_msg = "Azimuth must have a value between 0-360.\n"

        self.H_msg = ""
        if self.checkH() == False: self.H_msg = "Height must have a value between 0-90.\n"

        self.Rot_msg = ""
        if self.checkRot() == False: self.Rot_msg = "Height must have a value between 0-90.\n"
         
        
        if self.checkInput() == False:
                error = self.WoV_msg + self.Az_msg + self.H_msg + self.Rot_msg
                QMessageBox.warning(self, "Input error", error, QMessageBox.Cancel)
        
        else:   
                f = open("config/camera.txt", "w")
                data = [self.WoV, self.Az, self.H, self.Rot]     
                for p in data:
                        f.write(p+os.linesep)        
        
                f.close() 
                self.close()

    def is_number(self,s):
            try:
                float(s)
                return True
            except ValueError:
                return False    
                    
    def checkInput(self):
        return (self.checkWoV() and self.checkAz() and self.checkH() and self.checkRot())        
        
    def checkWoV(self):
        check = []
        for i in range (0, 361):
                check.append(str(i))
        if self.WoV in check: return True
        else: return False
                
    def checkAz(self):
        check = []
        for i in range (0, 181):
                check.append(str(i))
        if self.Az in check: return True
        else: return False
    
    def checkH(self):
        check = []
        for i in range (0, 91):
                check.append(str(i))
        if self.H in check: return True
        else: return False
    
    def checkRot(self):
        check = []
        for i in range (0, 91):
                check.append(str(i))
        if self.Rot in check: return True
        else: return False
    
class BrowseWindow(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 450, 200)
        self.setWindowTitle('Browse')
        self.setFixedSize(self.size())
        self.path = str(QFileDialog.getExistingDirectory())
        
        self.lbl0 = QLabel("Current Path: "+ self.path, self)
        self.lbl0.move(50, 20)   


        self.lbl1 = QLabel("Save current path?", self)
        self.lbl1.move(160, 70)


        

        OK = QPushButton('OK', self)
        OK.resize(150, 50)
        OK.move(50, 110)
        OK.clicked.connect(self.okButton)

        Cancel = QPushButton('Cancel', self)
        Cancel.resize(150, 50)
        Cancel.move (250, 110)
        Cancel.clicked.connect(self.cancelButton)
        
    def cancelButton(self):
        self.close()
        
    def okButton(self):
        f = open("config/browse.txt", "w")
        f.write(self.path)
        f.close()
        self.close()     


class MainWindow(QMainWindow):
    
    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.initUI()
        
        
    def initUI(self):

        
        #toolbar init
        CameraAct = QAction(QIcon('icons/fov.png'), 'Field of View', self)
        CameraAct.setShortcut('Ctrl+F')
        CameraAct.triggered.connect(self.camera)

        BrowseAct = QAction(QIcon('icons/browse.png'), 'Browse for folder', self)
        BrowseAct.setShortcut('Ctrl+B')
        BrowseAct.triggered.connect(self.browse)
        
        self.toolbar = self.addToolBar('Field of View')
        self.toolbar.addAction(CameraAct)
       
        self.toolbar = self.addToolBar('Browse')
        self.toolbar.addAction(BrowseAct)

        #window init
        self.width = 340
        self.height = 350        
        self.setGeometry(300, 300, self.width, self.height)
        self.setFixedSize(self.size())
        self.setWindowTitle('PMG camera')
        self.setWindowIcon(QIcon("fov.png")) 
        self.center()  
        

        #date1 input init

        self.lbl1 = QLabel("Start Time:", self)
        self.lbl1.move(70, 40)
        self.d1 = QComboBox(self)
        for day in range (1, 32):
                if day < 10:    
                        date = "0" + str(day)
                else: date = str(day)  
                self.d1.addItem(str(date))
        self.d1.resize(50, 30)        
        self.d1.move(20, 70)

        self.m1 = QComboBox(self)
        for month in range (1, 13):   
                if month < 10:
                        date = "0" + str(month)
                else: date = str(month)   
                self.m1.addItem(date)
        self.m1.resize(50, 30)        
        self.m1.move(70, 70)

        self.y1 = QComboBox(self)
        for year in range (2000, 2051):      
                self.y1.addItem(str(year))
        self.y1.resize(70, 30)        
        self.y1.move(120, 70)


        self.lbl2 = QLabel("Hrs.", self)
        self.lbl2.move(250, 40)
        self.hour1 = QLineEdit(self)
        self.hour1.move(250, 70)
        self.hour1.resize(30,30)

        self.lbl3 = QLabel("Mins.", self)
        self.lbl3.move(290, 40)
        self.min1 = QLineEdit(self)
        self.min1.move(290, 70)
        self.min1.resize(30,30)
        
        #date 2 input init
        move_down = 80
        
        self.lbl4 = QLabel("End Time:", self)
        self.lbl4.move(70, 120)
        self.d2 = QComboBox(self)
        for day in range (1, 32):      
                if day < 10:    
                        date = "0" + str(day)
                else: date = str(day)  
                self.d2.addItem(str(date))
        self.d2.resize(50, 30)        
        self.d2.move(20, 70+move_down)

        self.m2 = QComboBox(self)
        for month in range (1, 13):
                if month < 10:
                        date = "0" + str(month)
                else: date = str(month)                       
                self.m2.addItem(date)
        self.m2.resize(50, 30)        
        self.m2.move(70, 70+move_down)

        self.y2 = QComboBox(self)
        for year in range (2000, 2051):      
                self.y2.addItem(str(year))
        self.y2.resize(70, 30)        
        self.y2.move(120, 70+move_down)


        self.lbl5 = QLabel("Hrs.", self)
        self.lbl5.move(250, 120)
        self.hour2 = QLineEdit(self)
        self.hour2.resize(30,30)
        self.hour2.move(250, 70+move_down)
        
        self.lbl5 = QLabel("Mins.", self)
        self.lbl5.move(290, 120)
        self.min2 = QLineEdit(self)
        self.min2.resize(30,30)
        self.min2.move(290, 70+move_down)
        
        
        #Button init

        calc = QPushButton('Calculate', self)
        calc.resize(150, 50)
        calc.move(95, self.height-100)
        calc.clicked.connect(self.calculateButton)
        
        self.show()
        
        
    def camera(self):
        self.camera = CameraWindow()
        self.camera.show()

    def browse(self):
        self.B = BrowseWindow()
        self.B.show()
    
    
        

    def calculateButton(self):
        if self.checkHM() == False:
                error = "Hours must have values between 0-23.\nMinutes must have values between 0-59."
                QMessageBox.warning(self, "Input error", error, QMessageBox.Cancel)
        else:
                if self.checkYMD() == False:
                        error = "Start date must be older than End date."
                        QMessageBox.warning(self, "Input error", error, QMessageBox.Cancel)
                else:
                       
                        self.Banjo = (["2017-02-03 19:35:39", "11%"], ["2017-02-03 19:38:39", "21%"], ["2017-02-03 19:41:39", "39%"], ["2017-02-03 19:44:39", "56%"])

                        self.storeDates()
                        self.makeCSV()
                        #def BanjoRadiSvojaSranja() 
                        QMessageBox.information(self, "Success!", "Estimation was successful!", QMessageBox.Ok)
                        
    def storeDates(self):

        begin = str(self.d1.currentText()) + str(self.m1.currentText()) + str(self.y1.currentText()) + self.hour1.text() + self.min1.text()

        fbegin = open("config/begin.txt", "w")
        fbegin.write(begin)
        fbegin.close()

        end = str(self.d2.currentText()) + str(self.m2.currentText()) + str(self.y2.currentText()) + self.hour2.text() + self.min2.text()

        fend = open("config/end.txt", "w")
        fend.write(end)
        fend.close()
        
    def makeCSV(self):
                        
        code = self.Banjo[0][0]
        file_path = "tables/"+code+".csv"
        f = open(file_path, "w")
        f.write("time,cloudiness"+'\n')
        for info in self.Banjo:
                        data = str(info[0]) + "," + (info[1]) + '\n'
                        f.write(data)
        f.close()
        
    def is_number(self,s):
            try:
                int(s)
                return True
            except ValueError:
                return False            
    
    def checkHM(self):
        check = True
        
        h1 = self.hour1.text()
        h2 = self.hour2.text()

        m1 = self.min1.text()
        m2 = self.min2.text()

        if (m1 == "00"): m1 = "0"
        if (m2 == "00"): m2 = "0"

        hours = []
        for i in range(0, 24):
                hours.append(str(i))
        
        mins = []
        for i in range(0, 60):
                mins.append(str(i))
 
        if (h1 in hours) and (h2 in hours):
                check = True
        else:
                check = False
                return check

        if (m1 in mins) and (m2 in mins):
                check = True
        else:
                check = False
                return check
      
       
        
    def checkYMD(self):
        check = True

        year1 = int(self.y1.currentText())
        year2 = int(self.y2.currentText())

        month1 = int(self.m1.currentText())
        month2 = int(self.m2.currentText())

        day1 = int(self.d1.currentText())
        day2 = int(self.d2.currentText())

        hour1 = self.hour1.text()
        hour2 = self.hour2.text()

        min1 = self.min1.text()
        min2 = self.min2.text()

        
        
        if (year1 > year2):
                check = False
                return check
        if (year1 == year2):
                if(month1 > month2): 
                        check = False
                        return check
                if(month1 == month2):
                        if(day1 > day2):
                                check = False
                                return check
                        if(day1 == day2):
                                if (hour1 > hour2):
                                        check = False
                                        return check
                                if (hour1 == hour2):
                                        if(min1 >= min2):
                                                check = False
                                                return check
                                
        return check
                        
    def closeEvent(self, event):
        
        reply = QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QMessageBox.Yes | 
            QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore() 
     
    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())
