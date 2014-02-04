from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *
import sqlite3
import random

import sys

class MainScreenWindow(QMainWindow):
    def __init__ (self):
        super().__init__()



        self.setWindowTitle("Primary Maths Game - Main Menu Window")
        self.create_game_interface()
        self.create_options_screen_layouts()
        self.create_database_screen()
        self.adding_student_layout()
        self.change_student_records_intermediate()
        self.delete_student_layout()
        self.create_main_screen_layouts()

        self.stacked_layout = QStackedLayout() 
        self.stacked_layout.addWidget(self.Main_Screen_widget) #1
        self.stacked_layout.addWidget(self.Options_widget) #2
        self.stacked_layout.addWidget(self.game_widget) #3
        self.stacked_layout.addWidget(self.table_widget) #4
        self.stacked_layout.addWidget(self.adding_student_widget) #5
        self.stacked_layout.addWidget(self.changing_intermediate_widget) #6
        self.stacked_layout.addWidget(self.deleting_student_widget) #7

        self.central_widget = QWidget()
        self.central_widget.setLayout(self.stacked_layout)
        self.setCentralWidget(self.central_widget)

        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("Primary Maths Game.db")
        self.db.open()
        
        
        
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
        self.database_button.clicked.connect(self.changing_to_database)

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
        self.change_record_button.clicked.connect(self.changing_to_intermediate)

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
        self.bottom_bottom_layout = QHBoxLayout()

        self.layout.addLayout(self.top_layout)
        self.layout.addLayout(self.under_top_layout)
        self.layout.addLayout(self.middle_layout)
        self.layout.addLayout(self.bottom_layout)
        self.layout.addLayout(self.bottom_bottom_layout)
        
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


        
        self.top_layout.addWidget(self.PrimaryMathsTitle)
        self.under_top_layout.addWidget(self.QuestionLabel)
        self.middle_layout.addWidget(self.SmallQuestionLabel,0,0)
        self.middle_layout.addWidget(self.QuestionDisplay,0,1)
        self.middle_layout.addWidget(self.AnswerLabel,1,0)
        self.middle_layout.addWidget(self.AnswerLine,1,1)
        self.bottom_layout.addWidget(self.submit_answer_button,0,0)
        self.bottom_layout.addWidget(self.clear_answer_button,0,1)
        self.bottom_bottom_layout.addWidget(self.Quit_Button)

        self.game_widget.setMinimumSize(QSize(450,300))

        self.Quit_Button.clicked.connect(self.main_screen_back)
        self.submit_answer_button.clicked.connect(self.questions)

        return QuestionNumber

    def create_database_screen(self):
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("Primary Maths Game.db")
        self.db.open()

        self.back_button = QPushButton("Back")

        self.table_view = QTableView()
        self.over_layout = QGridLayout()
        self.table_layout = QVBoxLayout()
        self.under_layout = QGridLayout()

        self.table_layout.addWidget(self.table_view)
        self.under_layout.addWidget(self.back_button,0,0)

        self.over_layout.addLayout(self.table_layout,1,1)
        self.over_layout.addLayout(self.under_layout,2,1)

        self.table_widget = QWidget()
        self.table_widget.setLayout(self.over_layout)

        self.model = QSqlTableModel()
        self.model.setTable("Student")
        self.table_view.setModel(self.model)
        self.table_view.model().select()
        self.model.select()

        self.back_button.clicked.connect(self.main_screen_back)
        
    def adding_student_layout(self):
         
        self.add_button = QPushButton("Add Student")
        self.AddFont = QFont()
        self.AddFont.setPointSize(10)
        self.add_button.setFont(self.AddFont)
        self.add_button.setMinimumSize(30,30)
        self.clear_data_button = QPushButton("Clear")
        self.Clear_dataFont = QFont()
        self.Clear_dataFont.setPointSize(10)
        self.clear_data_button.setFont(self.Clear_dataFont)
        self.clear_data_button.setMinimumSize(30,30)
        self.Quit_Button = QPushButton("Quit")
        self.Quit_Button_Font = QFont()
        self.Quit_Button_Font.setPointSize(10)
        self.Quit_Button.setFont(self.Quit_Button_Font)
        self.Quit_Button.setMinimumSize(30,30)

        self.layout = QVBoxLayout()
        self.Under_Layout = QGridLayout()

        self.layout.addLayout(self.Under_Layout)

        self.StudentNameLabel = QLabel("Student Name:")
        StudentNameFont = QFont()
        StudentNameFont.setPointSize(15)
        self.StudentNameLabel.setFont(StudentNameFont)

        self.StudentNameAnswer = QLineEdit()
        StudentNameAnswerFont = QFont()
        StudentNameAnswerFont.setPointSize(15)
        self.StudentNameAnswer.setFont(StudentNameAnswerFont)

        self.StudentAbilityIDLabel = QLabel("Student Ability:")
        StudentAbilityFont = QFont()
        StudentAbilityFont.setPointSize(15)
        self.StudentAbilityIDLabel.setFont(StudentAbilityFont)

        self.StudentAbilityIDAnswer = QLineEdit()
        self.StudentAbilityIDAnswer.setFont(StudentAbilityFont)

        self.TeacherIDLabel = QLabel("Teacher ID:")
        self.TeacherIDLabel.setFont(StudentAbilityFont)

        self.TeacherIDAnswer = QLineEdit()
        self.TeacherIDAnswer.setFont(StudentAbilityFont)

        self.SchoolIDLabel = QLabel("School ID:")
        self.SchoolIDLabel.setFont(StudentAbilityFont)

        self.SchoolIDAnswer = QLineEdit()
        self.SchoolIDAnswer.setFont(StudentAbilityFont)


        self.Under_Layout.addWidget(self.StudentNameLabel,0,0)
        self.Under_Layout.addWidget(self.StudentNameAnswer,0,1)
        self.Under_Layout.addWidget(self.StudentAbilityIDLabel,1,0)
        self.Under_Layout.addWidget(self.StudentAbilityIDAnswer,1,1)
        self.Under_Layout.addWidget(self.TeacherIDLabel,2,0)
        self.Under_Layout.addWidget(self.TeacherIDAnswer,2,1)
        self.Under_Layout.addWidget(self.SchoolIDLabel,3,0)
        self.Under_Layout.addWidget(self.SchoolIDAnswer,3,1)
        self.Under_Layout.addWidget(self.add_button,4,0)
        self.Under_Layout.addWidget(self.clear_data_button,4,1)
        self.Under_Layout.addWidget(self.Quit_Button,4,2)

        self.adding_student_widget = QWidget()
        self.adding_student_widget.setLayout(self.layout)

        
        self.add_button.clicked.connect(self.adding_student_to_database)
        self.clear_data_button.clicked.connect(self.clearing_data)
        self.Quit_Button.clicked.connect(self.changing_to_options)

    def delete_student_layout(self):
        self.delete_button = QPushButton("Delete Student")
        self.DeleteFont = QFont()
        self.DeleteFont.setPointSize(10)
        self.delete_button.setFont(self.DeleteFont)
        self.delete_button.setMinimumSize(30,30)
        self.Quit_Button = QPushButton("Quit")
        self.Quit_Button_Font = QFont()
        self.Quit_Button_Font.setPointSize(10)
        self.Quit_Button.setFont(self.Quit_Button_Font)
        self.Quit_Button.setMinimumSize(30,30)

        self.layout = QVBoxLayout()
        self.Under_Layout = QGridLayout()

        self.layout.addLayout(self.Under_Layout)

        with sqlite3.connect("Primary Maths Game.db") as db:
            self.cursor = db.cursor()
            self.cursor.execute("select StudentName from Student")
            StudentList = []
            for each1 in self.cursor.fetchall():
                for each2 in each1:
                    StudentList.append(each2)


        self.student = QLabel("Student Name/ID")
        self.student_name_dropdown = QComboBox()
        for each in StudentList:
            self.student_name_dropdown.addItem(each)

        self.Under_Layout.addWidget(self.student,0,0)
        self.Under_Layout.addWidget(self.student_name_dropdown,0,1)
        self.Under_Layout.addWidget(self.delete_button,1,0)
        self.Under_Layout.addWidget(self.Quit_Button,1,1)

        self.deleting_student_widget = QWidget()
        self.deleting_student_widget.setLayout(self.layout)

        self.delete_button.clicked.connect(self.deleting_student_from_database)
        self.Quit_Button.clicked.connect(self.changing_to_options)
        

    def change_student_records_intermediate(self):
        self.adding_student_button = QPushButton("Add A Student")
        self.deleting_student_button = QPushButton("Delete A Student")
        self.updating_student_button = QPushButton("Update A Student")
        self.back_button = QPushButton("Back")

        self.layout = QGridLayout()
        self.middleLayout = QHBoxLayout()
        self.underLayout = QHBoxLayout()

        self.layout.addLayout(self.middleLayout,0,0)
        self.layout.addLayout(self.underLayout,1,0)

        self.middleLayout.addWidget(self.adding_student_button)
        self.middleLayout.addWidget(self.deleting_student_button)
        self.middleLayout.addWidget(self.updating_student_button)
        self.underLayout.addWidget(self.back_button)

        self.changing_intermediate_widget = QWidget()
        self.changing_intermediate_widget.setLayout(self.layout)

        self.adding_student_button.clicked.connect(self.changing_to_adding)
        self.deleting_student_button.clicked.connect(self.changing_to_deleting)
        self.back_button.clicked.connect(self.changing_to_options)

    def adding_student_to_database(self):
        query = QSqlQuery()
        Name = self.StudentNameAnswer.text()
        StudentAbility = self.StudentAbilityIDAnswer.text()
        TeacherID = self.TeacherIDAnswer.text()
        SchoolID = self.SchoolIDAnswer.text()
        query.prepare("""INSERT INTO Student (SchoolID, TeacherID, StudentAbilityID, StudentName) VALUES (?,?,?,?)""")
        query.bindValue(0, SchoolID)
        query.bindValue(1, TeacherID)
        query.bindValue(2, StudentAbility)
        query.bindValue(3, Name)
        query.exec_()
        self.clearing_data()
        print(query.lastError().text())

    def deleting_student_from_database(self):
        query = QSqlQuery()
        deleting = str(self.student_name_dropdown.currentText())
        self.student_name_dropdown.removeItem(self.student_name_dropdown.currentIndex())
        query.prepare("""DELETE FROM Student where StudentName = ?""")
        query.bindValue(0, deleting)
        query.exec_()
        print(query.lastError().text())

    def clearing_data(self):
        self.StudentAbilityIDAnswer.clear()
        self.TeacherIDAnswer.clear()
        self.SchoolIDAnswer.clear()
        self.StudentNameAnswer.clear()



    def question_generator(self):
        FirstNumber = random.randint(0,20)
        SecondNumber = random.randint(0,20)
        SignGenerator = random.randint(1,4)
        Signs = []
        Signs.append("+")
        Signs.append("-")
        Signs.append("*")
        Signs.append("/")
        Sign = Signs[SignGenerator]

        return FirstNumber, SecondNumber, Sign

    def questions(self,QuestionNumber,FirstNumber,SecondNumber,Sign):
        QuestionNumber += 1
        while QuestionNumber <= 20:
            Question = ("{0},{1},{2}".format(FirstNumber, Sign, SecondNumber))


    def main_screen_back(self):
        self.setWindowTitle("Primary Maths Game - Main Menu Window")
        self.stacked_layout.setCurrentIndex(0)

    def changing_to_options(self):
        self.setWindowTitle("Primary Maths Game - Options Window")
        self.stacked_layout.setCurrentIndex(1)
        
    def changing_to_game(self):
        self.setWindowTitle("Primary Maths Game - Game Window")
        self.stacked_layout.setCurrentIndex(2)

    def changing_to_database(self):
        self.setWindowTitle("Primary Maths Game - Database Window")
        self.stacked_layout.setCurrentIndex(3)
        self.model.refresh()

    def changing_to_adding(self):
        self.setWindowTitle("Primary Maths Game - Database Window: Adding")
        self.stacked_layout.setCurrentIndex(4)

    def changing_to_intermediate(self):
        self.setWindowTitle("Primary Maths Game - Database Window: Intermediate")
        self.stacked_layout.setCurrentIndex(5)

    def changing_to_deleting(self):
        self.setWindowTitle("Primary Maths Game - Database Window: Deleting")
        self.stacked_layout.setCurrentIndex(6)

def main():
    application = QApplication(sys.argv)
    window = MainScreenWindow()
    window.show()
    window.raise_()
    application.exec_()
    
            

if __name__ == "__main__":
    main()
