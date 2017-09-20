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
        check = True
        if self.is_number(self.WoV)==False:
                check = False
                #return check
        if float(self.WoV) < 0 or float(self.WoV) > 180:
                check = False                
                return check
        return check    

    def checkAz(self):
        check = True
        if self.is_number(self.Az)==False:
                check = False
                return check
        if float(self.Az) < 0 or float(self.Az) > 360:
                check = False                
                return check
        return check

    def checkH(self):
        check = True
        if self.is_number(self.H)==False:
                check = False
                return check
        if float(self.H) < 0 or float(self.H) > 90:
                check = False                
                return check
        return check

    def checkRot(self):
        check = True
        if self.is_number(self.Rot)==False:
                check = False
                return check
        if float(self.Rot) < 0 or float(self.Rot) > 90:
                check = False                
                return check
        return check

class BrowseWindow(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 450, 200)
        self.setWindowTitle('Browse')
        self.setFixedSize(self.size())
        files = str(QFileDialog.getExistingDirectory())
        
        self.lbl0 = QLabel("Current Path: "+ files, self)
        self.lbl0.move(10, 20)   


        f = open("config/browse.txt", "w")
        f.write(files)
        f.close()

        OK = QPushButton('OK', self)
        OK.resize(150, 50)
        OK.move(50, 110)
        OK.clicked.connect(self.okButton)

        
    def okButton(self):
        self.close()     

class CalcWindow(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 450, 200)
        self.setWindowTitle('Table')
        self.setFixedSize(self.size())

        
        OK = QPushButton('OK', self)
        OK.resize(150, 50)
        OK.move(50, 110)
        OK.clicked.connect(self.okButton)


        self.camera = open("config/camera.txt", "r").read().splitlines()
        
        self.browse = open("config/browse.txt", "r").read().splitlines()        
        self.save = open("config/save.txt", "r").read().splitlines()

        self.begin = open("config/begin.txt", "r").read().splitlines()

        self.end = open("config/end.txt", "r").read().splitlines()
    
    #def BanjoRadiSvojaSranja()    
                
    
    def okButton(self):
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
        
        self.toolbar = self.addToolBar('Camera')
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
                self.d1.addItem(str(day))
        self.d1.resize(50, 30)        
        self.d1.move(20, 70)

        self.m1 = QComboBox(self)
        for month in range (1, 13):      
                self.m1.addItem(str(month))
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
                self.d2.addItem(str(day))
        self.d2.resize(50, 30)        
        self.d2.move(20, 70+move_down)

        self.m2 = QComboBox(self)
        for month in range (1, 13):      
                self.m2.addItem(str(month))
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
                error = "Hours must have values between 0-24.\nMinutes must have values between 0-60."
                QMessageBox.warning(self, "Input error", error, QMessageBox.Cancel)
        else:
                if self.checkYMD() == False:
                        error = "Start date must me older than End date."
                        QMessageBox.warning(self, "Input error", error, QMessageBox.Cancel)
                else:
                        #print (10 + int(self.y1.currentText())) 
                        self.Banjo = (["2017-02-03 19:35:39", "11%"], ["2017-02-03 19:38:39", "21%"], ["2017-02-03 19:41:39", "39%"], ["2017-02-03 19:44:39", "56%"])

                        self.storeDates()
                        self.makeCSV()
                        self.C = CalcWindow()
                        self.C.show()
                        
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
        
        if(self.is_number(h1) == False) or (self.is_number(h2) == False) or (self.is_number(m1) == False) (self.is_number(m2) == False):
                
                check = False
                return check
        if(int(h1) < 0 and int(h1) > 24) or (int(h2) < 0 and int(h2) > 24) or (int(m1) < 0 and int(m1) > 60) or (int(m2) < 0 and int(m2) > 60):
                check = False
                return check
        return check
        
    def checkYMD(self):
        check = True

        year1 = int(self.y1.currentText())
        year2 = int(self.y2.currentText())

        month1 = int(self.m1.currentText())
        month2 = int(self.m2.currentText())

        day1 = int(self.d1.currentText())
        day2 = int(self.d2.currentText())

        hour1 = int(self.hour1.text())
        hour2 = int(self.hour2.text())

        min1 = int(self.min1.text())
        min1 = int(self.min2.text())
        
        if (year1 > year2):
                check = False
                return check
        if (year1 == year2):
                if(month1 > month2): 
                        check = False
                        return check
                if(month1 == month2):
                        if(day1 >= day2):
                                check = False
                                return check
        return check
                        
#vratiti sranje iz todo.py ovde
    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())
