import sys
import typing
import os
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QWidget, QApplication
import design

class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btnBrowse.clicked.connect(self.browse_file)

    def browse_file(self):
          self.listWidget.clear()
          directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Choose file")

          if directory:
                for file_name in os.listdir(directory):
                      self.listWidget.addItem(file_name)

def main():
        app = QtWidgets.QApplication(sys.argv)
        window = ExampleApp()
        window.show()
        app.exec_()

if __name__ == '__main__':
        main()
