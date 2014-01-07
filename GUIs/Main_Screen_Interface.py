from PyQt4.QtCore import *
from PyQt4.QtGui import *

import sys

class MainScreenWindow(QMainWindow):
    def __init__ (self):
        super().__init__()

        self.setWindowTitle("Primary Maths Game - Main Menu Window")

        
        self.start_game_button = QPushButton("Start Game")
        self.startFont = QFont()
        self.startFont.setPointSize(13)
        self.start_game_button.setFont(self.startFont)
        self.start_game_button.setMinimumSize(50,50)
        self.database_button = QPushButton("Database Of School Data")
        self.databaseFont = QFont()
        self.databaseFont.setPointSize(13)
        self.database_button.setFont(self.databaseFont)
        self.database_button.setMinimumSize(50,50)
        self.options_button = QPushButton("Options/Help")
        self.optionsFont = QFont()
        self.optionsFont.setPointSize(13)
        self.options_button.setFont(self.optionsFont)
        self.options_button.setMinimumSize(50,50)

        self.Main_Screen_layout = QVBoxLayout()
        self.bottom_layout = QGridLayout()
        self.middle_layout = QGridLayout()
        self.top_layout = QHBoxLayout()

        self.Main_Screen_layout.addLayout(self.top_layout)
        self.Main_Screen_layout.addLayout(self.middle_layout)
        self.Main_Screen_layout.addLayout(self.bottom_layout)

        self.Main_Screen_widget = QWidget()
        self.Main_Screen_widget.setLayout(self.Main_Screen_layout)

        self.PrimaryMathsTitle = QLabel("Primary Maths Game")
        self.PrimaryMathsTitle.setAlignment(Qt.AlignCenter)
        
        PrimaryMathsTitleFont = QFont()
        PrimaryMathsTitleFont.setPointSize(15)
        PrimaryMathsTitleFont.setBold(True)
        self.PrimaryMathsTitle.setFont(PrimaryMathsTitleFont)
        
        self.top_layout.addWidget(self.PrimaryMathsTitle)
        self.middle_layout.addWidget(self.start_game_button,0,1)
        self.middle_layout.addWidget(self.database_button,1,1)
        self.middle_layout.addWidget(self.options_button,2,1)
        

        self.setCentralWidget(self.Main_Screen_widget)
        self.Main_Screen_widget.setMinimumSize(QSize(450,300))

if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = MainScreenWindow()
    window.show()
    window.raise_()
    application.exec_()
