from PyQt5 import QtWidgets, uic
import sys
from ui.dialogs import MainUi


def main():
    app = QtWidgets.QApplication(sys.argv)
    
    window = MainUi()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()