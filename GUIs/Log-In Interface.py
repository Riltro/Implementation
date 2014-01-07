from PyQt4.QtCore import *
from PyQt4.QtGui import *

import sys

class LogInWindow(QMainWindow):
    def __init__ (self):
        super().__init__()

        self.setWindowTitle("Primary Maths Game - Log In Window")

        self.login_button = QPushButton("Login")
        self.clear_button = QPushButton("Clear")
        self.create_button = QPushButton("Create")

        self.layout = QVBoxLayout()
        self.bottom_layout = QGridLayout()
        self.middle_layout = QGridLayout()
        self.top_layout = QHBoxLayout()

        self.layout.addLayout(self.top_layout)
        self.layout.addLayout(self.middle_layout)
        self.layout.addLayout(self.bottom_layout)

        self.widget = QWidget()
        self.widget.setLayout(self.layout)

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

        self.setCentralWidget(self.widget)
        self.widget.setMinimumSize(QSize(400,200))

if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = LogInWindow()
    window.show()
    window.raise_()
    application.exec_()
        
        
        

        
