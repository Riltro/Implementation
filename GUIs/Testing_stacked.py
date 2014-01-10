from PyQt4.QtCore import *
from PyQt4.QtGui import *

import sys

self.change_record_button = QPushButton("Change Student's Record")
self.change_recordFont = QFont()
self.change_recordFont.setPointSize(13)
self.change_record_button.setFont(self.change_recordFont)
self.change_record_button.setMinimumSize(10,30)
self.change_difficulty_button = QPushButton("Change Game Difficulty")
self.change_difficultyFont = QFont()
self.change_difficultyFont.setPointSize(13)
self.change_difficulty_button.setFont(self.change_difficultyFont)
self.change_difficulty_button.setMinimumSize(10,30)
self.clear_data_button = QPushButton("Clear all data from school file")
self.clear_dataFont = QFont()
self.clear_dataFont.setPointSize(13)
self.clear_data_button.setFont(self.clear_dataFont)
self.clear_data_button.setMinimumSize(10,30)

self.layout = QVBoxLayout()
self.bottom_layout = QGridLayout()
self.middle_layout = QGridLayout()
self.top_layout = QHBoxLayout()

self.layout.addLayout(self.top_layout)
self.layout.addLayout(self.middle_layout)
self.layout.addLayout(self.bottom_layout)

self.Options_widget = QWidget()
self.Options_widget.setLayout(self.layout)

self.PrimaryMathsTitle = QLabel("Primary Maths Game (Options)")
self.PrimaryMathsTitle.setAlignment(Qt.AlignCenter)

PrimaryMathsTitleFont = QFont()
PrimaryMathsTitleFont.setPointSize(15)
PrimaryMathsTitleFont.setBold(True)
self.PrimaryMathsTitle.setFont(PrimaryMathsTitleFont)

#self.OptionsTitle = QLabel("Options")
#self.OptionsTitle.setAlignment(Qt.AlignCenter|Qt.AlignBottom)

#self.OptionsTitle.setFont(PrimaryMathsTitleFont)        

self.top_layout.addWidget(self.PrimaryMathsTitle)
#self.top_layout.addWidget(self.OptionsTitle)
self.middle_layout.addWidget(self.change_difficulty_button,0,1)
self.middle_layout.addWidget(self.change_record_button,1,1)
self.middle_layout.addWidget(self.clear_data_button,2,1)


self.setCentralWidget(self.Options_widget)
self.Options_widget.setMinimumSize(QSize(450,300))
