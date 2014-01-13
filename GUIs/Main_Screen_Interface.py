from PyQt4.QtCore import *
from PyQt4.QtGui import *

import sys

class MainScreenWindow(QMainWindow):
    def __init__ (self):
        super().__init__()



        self.setWindowTitle("Primary Maths Game - Main Menu Window")
        self.create_game_interface()
        self.create_options_screen_layouts()
        self.create_main_screen_layouts()

        self.stacked_layout = QStackedLayout()
        self.stacked_layout.addWidget(self.Main_Screen_widget)
        self.stacked_layout.addWidget(self.Options_widget)
        self.stacked_layout.addWidget(self.game_widget)

        self.central_widget = QWidget()
        self.central_widget.setLayout(self.stacked_layout)
        self.setCentralWidget(self.central_widget)
        
        
        
    def create_main_screen_layouts(self):
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
        
        self.Main_Screen_widget.setMinimumSize(QSize(450,300))

        self.options_button.clicked.connect(self.changing_to_options)
        self.start_game_button.clicked.connect(self.changing_to_game)

    def create_options_screen_layouts(self):
        self.setWindowTitle("Primary Maths Game - Main Menu Window")
        
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
        self.back_button = QPushButton("Back")
        self.back_font = QFont()
        self.back_font.setPointSize(10)
        self.back_button.setFont(self.back_font)
        self.back_button.setMinimumSize(15,15)

        self.layout = QVBoxLayout()
        self.bottom_layout = QGridLayout()
        self.middle_layout = QGridLayout()
        self.top_layout = QHBoxLayout()

        self.layout.addLayout(self.top_layout)
        self.layout.addLayout(self.middle_layout)
        self.layout.addLayout(self.bottom_layout)

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
        self.bottom_layout.addWidget(self.back_button,0,2)
        

        self.Options_widget = QWidget()
        self.Options_widget.setLayout(self.layout)

        
        self.Options_widget.setMinimumSize(QSize(450,300))

        self.back_button.clicked.connect(self.main_screen_back)

    def create_game_interface(self):

        QuestionNumber = 1
        Question = "10 + 10 = ?"
        #Actual_Question = get_question()

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
        self.Quit_Button = QPushButton("Quit")
        self.Quit_Button_Font = QFont()
        self.Quit_Button_Font.setPointSize(10)
        self.Quit_Button.setFont(self.Quit_Button_Font)
        self.Quit_Button.setMinimumSize(30,30)

        self.layout = QVBoxLayout()
        self.bottom_layout = QGridLayout()
        self.middle_layout = QGridLayout()
        self.top_layout = QHBoxLayout()
        self.under_top_layout = QHBoxLayout()
        self.top_top_layout = QGridLayout()

        self.layout.addLayout(self.top_top_layout)
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

        self.game_widget = QWidget()
        self.game_widget.setLayout(self.layout)


        self.top_top_layout.addWidget(self.Quit_Button,2,0)
        self.top_layout.addWidget(self.PrimaryMathsTitle)
        self.under_top_layout.addWidget(self.QuestionLabel)
        self.middle_layout.addWidget(self.SmallQuestionLabel,0,0)
        self.middle_layout.addWidget(self.QuestionDisplay,0,1)
        self.middle_layout.addWidget(self.AnswerLabel,1,0)
        self.middle_layout.addWidget(self.AnswerLine,1,1)
        self.bottom_layout.addWidget(self.submit_answer_button,0,0)
        self.bottom_layout.addWidget(self.clear_answer_button,0,1)

        self.game_widget.setMinimumSize(QSize(450,300))

        self.Quit_Button.clicked.connect(self.main_screen_back)

        
    def main_screen_back(self):
        self.setWindowTitle("Primary Maths Game - Main Menu Window")
        self.stacked_layout.setCurrentIndex(0)

    def changing_to_options(self):
        self.setWindowTitle("Primary Maths Game - Options Window")
        self.stacked_layout.setCurrentIndex(1)
        
    def changing_to_game(self):
        self.setWindowTitle("Primary Maths Game - Game Window")
        self.stacked_layout.setCurrentIndex(2)

def main():
    application = QApplication(sys.argv)
    window = MainScreenWindow()
    window.show()
    window.raise_()
    application.exec_()
    
            

if __name__ == "__main__":
    main()
