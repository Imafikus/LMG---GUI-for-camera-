import sys
from PyQt5.QtWidgets import *#QApplication, QWidget, QMessageBox, qApp, QDesktopWidget, QMainWindow, QAction

from PyQt5.QtGui import *#QIcon


class Example(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):



        FOVAct = QAction(QIcon('icons/fov.png'), 'FOV', self)
        FOVAct.setShortcut('Ctrl+F')
        FOVAct.triggered.connect(self.do_thingy)

        CVPAct = QAction(QIcon('icons/cvp.png'), 'CVP', self)
        CVPAct.setShortcut('Ctrl+P')
        CVPAct.triggered.connect(self.do_thingy)

        BrowseAct = QAction(QIcon('icons/browse.png'), 'Browse', self)
        BrowseAct.setShortcut('Ctrl+B')
        BrowseAct.triggered.connect(self.do_thingy)

        SaveAct = QAction(QIcon('icons/save.png'), 'Browse', self)
        SaveAct.setShortcut('Ctrl+B')
        SaveAct.triggered.connect(self.do_thingy)
                

                

        self.toolbar = self.addToolBar('FOV')
        self.toolbar.addAction(FOVAct)

        self.toolbar = self.addToolBar('CVP')
        self.toolbar.addAction(CVPAct)

        self.toolbar = self.addToolBar('Browse')
        self.toolbar.addAction(BrowseAct)

        self.toolbar = self.addToolBar('Save')
        self.toolbar.addAction(SaveAct)

        
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon("fov.png")) 
        self.center()  
    
        self.show()
    
    def do_thingy(self):
        print("print")

    

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
    ex = Example()
    sys.exit(app.exec_())
