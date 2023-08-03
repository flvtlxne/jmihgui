import sys #for argv to QApplication
import typing
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QWidget, QApplication
import design #converted design.ui

class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        #for access to data in design.py 
        super().__init__()
        self.setupUi(self) #for initialize my design
    
def main():
        app = QtWidgets.QApplication(sys.argv)
        window = ExampleApp()
        window.show()
        app.exec_()

if __name__ == '__main__':
        main()
