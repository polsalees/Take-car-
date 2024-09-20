import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog 

class sign_upDlg(QDialog):
    """sign_up dialog."""
    def __init__(self, parent=None):
        super().__init__(parent)
        # Load the dialog's GUI
        loadUi("ui/sign_up.ui", self)

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        #Load the UI file directly
        uic.loadUi("ui/main_window.ui", self) #Path to the .ui file


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()   #Create an instant of the main window
window.show()   #Show the main window
app.exec_()     #Start the application event loop