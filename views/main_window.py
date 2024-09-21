# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import sys
from PyQt5 import uic, QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog
from sign_up import Ui_sign_up_dialog




class sign_up_window(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(sign_up_window, self).__init__(parent)
        self.ui = Ui_sign_up_dialog()  # Instantiate the generated UI class
        self.ui.setupUi(self)  # Set up the UI for this dialog window


class UI_MainWindow(object):
    def setupUi(self, MainWindow):
        # Setting up the main window's object name, size, and cursor
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 700)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setFocusPolicy(QtCore.Qt.NoFocus)

        # Central widget setup (this is the container for the rest of the UI)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        # Creating a widget for layout and positioning it
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(470, 100, 288, 264))
        self.widget.setObjectName("widget")
        
        # Vertical layout to stack elements in a column
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        # Label with palette and font setup for the title "Take Car!"
        self.label = QtWidgets.QLabel(self.widget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        self.label.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label.setAutoFillBackground(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        
        # Adding the label to the vertical layout
        self.verticalLayout.addWidget(self.label)

        # Creating a form layout for input fields (Username and Password)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        
        # Adding "Username" label and text input field
        self.username_label = QtWidgets.QLabel(self.widget)
        self.username_label.setObjectName("username_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.username_label)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit.setFont(font)
        self.lineEdit.setCursor(QtGui.QCursor(QtCore.Qt.SplitVCursor))
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)

        # Adding "Password" label and text input field
        self.password_label = QtWidgets.QLabel(self.widget)
        self.password_label.setObjectName("password_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.password_label)
        self.password_lineedit = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.password_lineedit.setFont(font)
        self.password_lineedit.setCursor(QtGui.QCursor(QtCore.Qt.SplitVCursor))
        self.password_lineedit.setObjectName("password_lineedit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.password_lineedit)

        # Adding the form layout to the vertical layout
        self.verticalLayout.addLayout(self.formLayout)

        # Creating the "SIGN-IN" button
        self.sign_in_button = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sign_in_button.setFont(font)
        self.sign_in_button.setObjectName("sign_in_button")
        
        # Adding "SIGN-IN" button to the vertical layout
        self.verticalLayout.addWidget(self.sign_in_button)

        # Sign Up button creation
        # --------------------------------------------
        # This is the button we'll connect to the function that opens another window (dialog).
        self.sign_up_button = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sign_up_button.setFont(font)
        self.sign_up_button.setObjectName("sign_up_button")

       # Connect the 'Sign Up' button to open the dialog window
        self.sign_up_button.clicked.connect(self.open_sign_up_dialog)
        
        # Adding the "SIGN-UP" button to the vertical layout
        self.verticalLayout.addWidget(self.sign_up_button)
        # --------------------------------------------

        # Other widgets and buttons (like options and exit)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(515, 380, 201, 31))
        self.widget1.setObjectName("widget1")
        self.formLayout_2 = QtWidgets.QFormLayout(self.widget1)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.options_button = QtWidgets.QPushButton(self.widget1)
        self.options_button.setObjectName("options_button")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.options_button)
        self.exit_button = QtWidgets.QPushButton(self.widget1)
        self.exit_button.setObjectName("exit_button")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.exit_button)

        # Set the central widget for the main window
        MainWindow.setCentralWidget(self.centralwidget)

        # Setup the menu bar and status bar
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1099, 26))
        self.menubar.setObjectName("menubar")
        self.menuTake_Car = QtWidgets.QMenu(self.menubar)
        self.menuTake_Car.setObjectName("menuTake_Car")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuTake_Car.menuAction())

        # Function to handle translating the UI texts (like button names, labels)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        # Set the text for each UI element
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Take Car!"))
        self.username_label.setText(_translate("MainWindow", "Username"))
        self.password_label.setText(_translate("MainWindow", "Password"))
        self.sign_in_button.setText(_translate("MainWindow", "SIGN-IN"))
        self.sign_up_button.setText(_translate("MainWindow", "SIGN-UP"))  # Label for the Sign-Up button
        self.options_button.setText(_translate("MainWindow", "OPTIONS"))
        self.exit_button.setText(_translate("MainWindow", "EXIT"))

    def open_sign_up_dialog(self):
        #Create an instance of the dialog and show it
        self.sign_up_dialog = sign_up_window()
        self.sign_up_dialog.show()

        
    

# Main execution logic
if __name__ == "__main__":
    import sys
    # Create the Qt application and the main window
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    
    # Initialize the UI for the main window
    ui = UI_MainWindow()
    ui.setupUi(MainWindow)
    
    # Show the main window
    MainWindow.show()
    
    # Execute the application's event loop
    sys.exit(app.exec_())
