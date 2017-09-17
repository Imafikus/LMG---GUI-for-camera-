import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import os



class FOVWindow(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 250, 400)
        self.setFixedSize(self.size())

        self.values = open("config/camera.txt").read().splitlines()
        
        #FOV part
        self.lbl1 = QLabel("FOV:", self)
        self.lbl1.move(20, 55)

        self.lbl2 = QLabel("Lat.", self)
        self.lbl2.move(80, 30)

        self.p1 = QLineEdit(self)
        self.p1.move(70, 50)
        self.p1.resize(45,30)
        self.p1.setText(self.values[0])
        
        #CVP part
        self.lbl3 = QLabel("CVP:", self)
        self.lbl3.move(20, 120)

        self.lbl4 = QLabel("Az.", self)
        self.lbl4.move(80, 95)

        self.p2 = QLineEdit(self)
        self.p2.move(70, 115)
        self.p2.resize(45,30)
        self.p2.setText(self.values[1])

        
        self.lbl5 = QLabel("H.", self)
        self.lbl5.move(140, 95)

        self.p3 = QLineEdit(self)
        self.p3.move(130, 115)
        self.p3.resize(45,30)
        self.p3.setText(self.values[2])
        
        #ROT part
        self.lbl3 = QLabel("CAM:", self)
        self.lbl3.move(20, 185)


        self.lbl6 = QLabel("Deg.", self)
        self.lbl6.move(80, 160)

        self.p4 = QLineEdit(self)
        self.p4.move(70, 180)
        self.p4.resize(45,30)
        self.p4.setText(self.values[3])



                
        OK = QPushButton('OK', self)
        OK.resize(150, 50)
        OK.move(50, 250)
        OK.clicked.connect(self.okButton)
        
    def okButton(self):
        p1 = self.p1.text()
        p2 = self.p2.text() 
        p3 = self.p3.text()
        p4 = self.p4.text()
        
        data = [p1, p2, p3, p4]  

        if self.checkInput(data) == False:
                QMessageBox.warning(self, "Cannot calculate",
                    "Please enter a valid number.", QMessageBox.Cancel) 

        else:   
                f = open("config/camera.txt", "w")     
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
                    
    def checkInput(self, data):
        check = True
        for p in data:
                if self.is_number(p) == False:
                        check = False
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

class SaveWindow(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 450, 200)
        self.setWindowTitle('Save')
        self.setWindowIcon(QIcon("save.png")) 
        self.setFixedSize(self.size())
        files = str(QFileDialog.getExistingDirectory())
			        
        self.lbl0 = QLabel("Save Path: "+ files, self)
        self.lbl0.move(10, 20)

        f = open("config/save.txt", "w")
        f.write(files)
        f.close()

        OK = QPushButton('OK', self)
        OK.resize(150, 50)
        OK.move(50, 110)
        OK.clicked.connect(self.okButton)

        
    def okButton(self):
        self.close()        
        
class MainWindow(QMainWindow):
    
    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.initUI()
        
        
    def initUI(self):

        
        #toolbar init
        FOVAct = QAction(QIcon('icons/camera.png'), 'Camera', self)
        FOVAct.setShortcut('Ctrl+F')
        FOVAct.triggered.connect(self.fov)

        BrowseAct = QAction(QIcon('icons/browse.png'), 'Browse', self)
        BrowseAct.setShortcut('Ctrl+B')
        BrowseAct.triggered.connect(self.browse)

        SaveAct = QAction(QIcon('icons/save.png'), 'Save', self)
        SaveAct.setShortcut('Ctrl+S')
        SaveAct.triggered.connect(self.save)
                
        
        self.toolbar = self.addToolBar('Camera')
        self.toolbar.addAction(FOVAct)
       
        self.toolbar = self.addToolBar('Browse')
        self.toolbar.addAction(BrowseAct)

        self.toolbar = self.addToolBar('Save')
        self.toolbar.addAction(SaveAct)

        #window init
        self.width = 340
        self.height = 350        
        self.setGeometry(300, 300, self.width, self.height)
        self.setFixedSize(self.size())
        self.setWindowTitle('PMG camera')
        self.setWindowIcon(QIcon("fov.png")) 
        self.center()  
        

        #date1 input init

        d1 = QComboBox(self)
        for day in range (1, 32):      
                d1.addItem(str(day)+".")
        d1.resize(50, 30)        
        d1.move(20, 70)

        m1 = QComboBox(self)
        for month in range (1, 13):      
                m1.addItem(str(month)+".")
        m1.resize(50, 30)        
        m1.move(70, 70)

        y1 = QComboBox(self)
        for year in range (2000, 2051):      
                y1.addItem(str(year)+".")
        y1.resize(70, 30)        
        y1.move(120, 70)

        hour1 = QLineEdit(self)
        hour1.move(250, 70)
        hour1.resize(30,30)

        min1 = QLineEdit(self)
        min1.move(290, 70)
        min1.resize(30,30)
        
        #date 2 input init
        move_down = 80

        d2 = QComboBox(self)
        for day in range (1, 32):      
                d2.addItem(str(day)+".")
        d2.resize(50, 30)        
        d2.move(20, 70+move_down)

        m2 = QComboBox(self)
        for month in range (1, 13):      
                m2.addItem(str(month)+".")
        m2.resize(50, 30)        
        m2.move(70, 70+move_down)

        y2 = QComboBox(self)
        for year in range (2000, 2051):      
                y2.addItem(str(year)+".")
        y2.resize(70, 30)        
        y2.move(120, 70+move_down)

        hour2 = QLineEdit(self)
        hour2.resize(30,30)
        hour2.move(250, 70+move_down)
        
        min2 = QLineEdit(self)
        min2.resize(30,30)
        min2.move(290, 70+move_down)
        
        
        #Button init
        calc = QPushButton('Calculate', self)
        calc.resize(150, 50)
        calc.move(95, self.height-100)
        calc.clicked.connect(self.calculateButton)
        
        self.show()
        
        
    def fov(self):
        self.FOV = FOVWindow()
        self.FOV.show()

    def browse(self):
        self.B = BrowseWindow()
        self.B.show()

    def save(self):
        self.S = SaveWindow()
        self.S.show()

    def calculateButton(self):
        
        camera = open("config/camera.txt", "r").read().splitlines()
        
        browse = open("config/browse.txt", "r").read().splitlines()        
        save = open("config/save.txt", "r").read().splitlines()

        settings = [camera, browse, save]
        
        

            

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
