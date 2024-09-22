from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QDialog

class MainUi(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/main.ui', self)
