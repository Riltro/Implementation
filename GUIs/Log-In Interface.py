from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Main_Screen_Interface import *

import sys

class LogInWindow(QMainWindow):
    def __init__ (self):
        super().__init__()

        self.setWindowTitle("Primary Maths Game - Log In Window")

        self.CentralWidget.setLayout(self.stacked_layout)

        self.login_button = QPushButton("Login")
        self.clear_button = QPushButton("Clear")
        self.create_button = QPushButton("Create")

        self.LogInlayout = QVBoxLayout()
        self.bottom_layout = QGridLayout()
        self.middle_layout = QGridLayout()
        self.top_layout = QHBoxLayout()

        self.Log_In_layout.addLayout(self.top_layout)
        self.Log_In_layout.addLayout(self.middle_layout)
        self.Log_In_layout.addLayout(self.bottom_layout)

        self.Log_In_widget = QWidget()
        self.Log_In_widget.setLayout(self.stacked_layout)
        

        self.StudentIDLabel = QLabel("Student ID")
        self.StudentIDLine = QLineEdit()
        self.StudentPasswordLabel = QLabel("Student Password")
        self.StudentPasswordLine = QLineEdit()
        self.PrimaryMathsTitle = QLabel("Primary Maths Game")
        self.PrimaryMathsTitle.setAlignment(Qt.AlignCenter)
        PrimaryMathsTitleFont = QFont()
        PrimaryMathsTitleFont.setPointSize(15)
        PrimaryMathsTitleFont.setBold(True)
        self.PrimaryMathsTitle.setFont(PrimaryMathsTitleFont)
        
        self.top_layout.addWidget(self.PrimaryMathsTitle)
        self.middle_layout.addWidget(self.StudentIDLabel,0,0)
        self.middle_layout.addWidget(self.StudentIDLine,0,1)
        self.middle_layout.addWidget(self.StudentPasswordLabel,1,0)
        self.middle_layout.addWidget(self.StudentPasswordLine,1,1)
        self.bottom_layout.addWidget(self.login_button,0,0)
        self.bottom_layout.addWidget(self.clear_button,0,1)
        self.bottom_layout.addWidget(self.create_button,0,2)

        self.setCentralWidget(self.Log_In_widget)
        self.Log_In_widget.setMinimumSize(QSize(400,200))
        self.stacked_layout = QStackedLayout()
        self.stacked_layout.addWidget(self.Log_In_Widget)
        self.stacked_layout.addWidget(self.Main_Screen_widget)

        self.login_button.clicked.connect(self.switching_layouts)

    def switching_layouts(self):
        self.stacked_layout.setCurrentIndex(1)

    
        

if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = LogInWindow()
    window.show()
    window.raise_()
    application.exec_()
        
        
        

        
