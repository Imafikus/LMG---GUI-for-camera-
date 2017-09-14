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

        self.width = 300
        self.height = 300
        
        self.setGeometry(300, 300, self.width, self.height)
        self.setFixedSize(self.size())
        self.setWindowTitle('PMG camera')
        self.setWindowIcon(QIcon("fov.png")) 
        self.center()  

        calc = QPushButton('Calculate', self)
        calc.resize(150, 50)
        calc.move(75, 200)
        


        
    
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
