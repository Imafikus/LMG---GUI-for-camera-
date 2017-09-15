import sys
from PyQt5.QtWidgets import *#QApplication, QWidget, QMessageBox, qApp, QDesktopWidget, QMainWindow, QAction

from PyQt5.QtGui import QIcon



class FOVWindow(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('FOV')
        self.setWindowIcon(QIcon("fov.png")) 

class CVPWindow(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('CVP')
        self.setWindowIcon(QIcon("fov.png")) 

class BrowseWindow(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Browse')
        self.setWindowIcon(QIcon("fov.png")) 

class SaveWindow(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Save')
        self.setWindowIcon(QIcon("fov.png")) 
        

        
class MainWindow(QMainWindow):
    
    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.initUI()
        
        
    def initUI(self):

        
        #toolbar init
        FOVAct = QAction(QIcon('icons/fov.png'), 'FOV', self)
        FOVAct.setShortcut('Ctrl+F')
        FOVAct.triggered.connect(self.fov)

        CVPAct = QAction(QIcon('icons/cvp.png'), 'CVP', self)
        CVPAct.setShortcut('Ctrl+P')
        CVPAct.triggered.connect(self.cvp)

        BrowseAct = QAction(QIcon('icons/browse.png'), 'Browse', self)
        BrowseAct.setShortcut('Ctrl+B')
        BrowseAct.triggered.connect(self.browse)

        SaveAct = QAction(QIcon('icons/save.png'), 'Save', self)
        SaveAct.setShortcut('Ctrl+S')
        SaveAct.triggered.connect(self.save)
                
        
        self.toolbar = self.addToolBar('FOV')
        self.toolbar.addAction(FOVAct)

        self.toolbar = self.addToolBar('CVP')
        self.toolbar.addAction(CVPAct)

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

    def cvp(self):
        self.CVP = CVPWindow()
        self.CVP.show()

    def browse(self):
        self.B = BrowseWindow()
        self.B.show()

    def save(self):
        self.S = SaveWindow()
        self.S.show()

    def calculateButton(self):
        print("Banjo")

    

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
