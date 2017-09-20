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
                int(s)
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
        if int(self.WoV) < 0 or int(self.WoV) > 180:
                check = False                
                return check
        return check    

    def checkAz(self):
        check = True
        if self.is_number(self.Az)==False:
                check = False
                return check
        if int(self.Az) < 0 or int(self.Az) > 360:
                check = False                
                return check
        return check

    def checkH(self):
        check = True
        if self.is_number(self.H)==False:
                check = False
                return check
        if int(self.H) < 0 or int(self.H) > 90:
                check = False                
                return check
        return check

    def checkRot(self):
        check = True
        if self.is_number(self.Rot)==False:
                check = False
                return check
        if int(self.Rot) < 0 or int(self.Rot) > 90:
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

        BrowseAct = QAction(QIcon('icons/browse.png'), 'Browse', self)
        BrowseAct.setShortcut('Ctrl+B')
        BrowseAct.triggered.connect(self.browse)

        """SaveAct = QAction(QIcon('icons/save.png'), 'Save', self)
        SaveAct.setShortcut('Ctrl+S')
        SaveAct.triggered.connect(self.save)
        """        
        
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

        self.hour1 = QLineEdit(self)
        self.hour1.move(250, 70)
        self.hour1.resize(30,30)

        self.min1 = QLineEdit(self)
        self.min1.move(290, 70)
        self.min1.resize(30,30)
        
        #date 2 input init
        move_down = 80

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

        self.hour2 = QLineEdit(self)
        self.hour2.resize(30,30)
        self.hour2.move(250, 70+move_down)
        
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
    """
        def closeEvent(self, event):
        
        reply = QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QMessageBox.Yes | 
            QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
    """     
    def center(self):
        
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())
