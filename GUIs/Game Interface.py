from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Question import *

import sys


class GameWindow(QMainWindow):
    def __init__ (self):
        super().__init__()

        QuestionNumber = 1
        Question = "10 + 10 = ?"
        #Actual_Question = get_question()
        
        self.setWindowTitle("Primary Maths Game - Game Window")

        self.submit_answer_button = QPushButton("Submit Answer")
        self.SubmitAnswerFont = QFont()
        self.SubmitAnswerFont.setPointSize(10)
        self.submit_answer_button.setFont(self.SubmitAnswerFont)
        self.submit_answer_button.setMinimumSize(30,30)
        self.clear_answer_button = QPushButton("Clear Answer")
        self.ClearAnswerFont = QFont()
        self.ClearAnswerFont.setPointSize(10)
        self.clear_answer_button.setFont(self.ClearAnswerFont)
        self.clear_answer_button.setMinimumSize(30,30)

        self.layout = QVBoxLayout()
        self.bottom_layout = QGridLayout()
        self.middle_layout = QGridLayout()
        self.top_layout = QHBoxLayout()
        self.under_top_layout = QHBoxLayout()

        self.layout.addLayout(self.top_layout)
        self.layout.addLayout(self.under_top_layout)
        self.layout.addLayout(self.middle_layout)
        self.layout.addLayout(self.bottom_layout)
        
        self.PrimaryMathsTitle = QLabel("Primary Maths Game")
        self.PrimaryMathsTitle.setAlignment(Qt.AlignCenter)
        self.PrimaryMathsTitle.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        
        PrimaryMathsTitleFont = QFont()
        PrimaryMathsTitleFont.setPointSize(15)
        PrimaryMathsTitleFont.setBold(True)
        self.PrimaryMathsTitle.setFont(PrimaryMathsTitleFont)

        self.QuestionLabel = QLabel("Question {0}".format(QuestionNumber))
        QuestionLabelFont = QFont()
        QuestionLabelFont.setPointSize(15)
        self.QuestionLabel.setFont(QuestionLabelFont)
        self.QuestionLabel.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.SmallQuestionLabel = QLabel("Question: ")
        SmallQuestionFont = QFont()
        SmallQuestionFont.setPointSize(15)
        self.SmallQuestionLabel.setFont(SmallQuestionFont)

        self.QuestionDisplay = QLabel("{0}".format(Question))
        QuestionDisplayFont = QFont()
        QuestionDisplayFont.setPointSize(20)
        self.QuestionDisplay.setFont(QuestionDisplayFont)
        self.QuestionDisplay.setAlignment(Qt.AlignCenter)

        self.AnswerLabel = QLabel("Answer: ")
        AnswerLabelFont = QFont()
        AnswerLabelFont.setPointSize(15)
        self.AnswerLabel.setFont(AnswerLabelFont)

        self.AnswerLine = QLineEdit()
        AnswerFont = QFont()
        AnswerFont.setPointSize(15)
        self.AnswerLine.setFont(AnswerFont)

        self.widget = QWidget()
        self.widget.setLayout(self.layout)

        self.top_layout.addWidget(self.PrimaryMathsTitle)
        self.under_top_layout.addWidget(self.QuestionLabel)
        self.middle_layout.addWidget(self.SmallQuestionLabel,0,0)
        self.middle_layout.addWidget(self.QuestionDisplay,0,1)
        self.middle_layout.addWidget(self.AnswerLabel,1,0)
        self.middle_layout.addWidget(self.AnswerLine,1,1)
        self.bottom_layout.addWidget(self.submit_answer_button,0,0)
        self.bottom_layout.addWidget(self.clear_answer_button,0,1)

        self.setCentralWidget(self.widget)
        self.widget.setMinimumSize(QSize(450,300))

if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = GameWindow()
    window.show()
    window.raise_()
    application.exec_()

        







        

        
