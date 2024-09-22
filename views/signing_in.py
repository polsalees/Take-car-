from PyQt5 import QtWidgets, QtGui

class signing_in_dialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("signing_in_dialog")
        self.setGeometry(100, 100, 400, 200)

        # Add UI elements to the dialog
        layout = QtWidgets.QVBoxLayout()
        
        self.label = QtWidgets.QLabel("Signing in...", self)
        # Change the font size of the label
        font = QtGui.QFont()
        font.setPointSize(16)  # Set the desired font size (e.g., 16)
        self.label.setFont(font)
        layout.addWidget(self.label)

        self.setLayout(layout)