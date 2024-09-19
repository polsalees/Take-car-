import sys
from PyQt5.QtWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Take Car!")
        self.setGeometry(100, 100, 1500, 900)  # Set the window size

        # Create central widget and layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # Add buttons
        self.button1 = QPushButton("Enter", self)
        self.button1.clicked.connect(self.option1_clicked)
        self.layout.addWidget(self.button1)

        self.exit_action = QPushButton("Exit", self)
        self.exit_action.clicked.connect(self.close)
        self.layout.addWidget(self.exit_action)


    def option1_clicked(self):
        print("Option 1 clicked")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
