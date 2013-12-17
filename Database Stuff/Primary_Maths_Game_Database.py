import sqlite3

def create_table(db_name,table_name,sql):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        cursor.execute("Select name from sqlite_master where name=?",(table_name,))
        result = cursor.fetchall()
        keep_table = True
        if len(result) == 1:
            response = input("The table {0} already exists, do you wish to recreate it? (y/n): ".format(table_name))
            if response == "y":
                keep_table = False
                print("The {0} table will be recreated; all existing data will be lost.".format(table_name))
                cursor.execute("Drop table if exists {0}".format(table_name))
                db.commit()
            else:
                print("The existing table was kept.")
        else:
            keep_table = False
        if not keep_table:
            cursor.execute(sql)
            db.commit


def create_game_table():
    sql = """create table Game
                (GameID integer,
                GameDescription text,
                primary key(GameID))"""
    create_table(db_name,"Game", sql)

def create_game_difficulty_table():
    sql = """create table GameDifficulty
                (DifficultyID integer,
                DifficultyDescription text,
                primary key(DifficultyID))"""
    create_table(db_name,"GameDifficulty", sql)

def create_attempt_table():
    sql = """create table Attempt
                (AttemptID integer,
                StudentID integer,
                GameID integer,
                DifficultyID integer,
                Score Integer,
                primary key(AttemptID)
                foreign key(StudentID) references Student(StudentID)
                foreign key(GameID) references Game(GameID)
                foreign key(DifficultyID) references GameDifficulty(DifficultyID))"""
    create_table(db_name,"Attempt", sql)

def create_student_table():
    sql = """create table Student
                (StudentID integer,
                SchoolID integer,
                TeacherID integer,
                StudentAbilityID integer,
                StudentName text,
                primary key(StudentID)
                foreign key(SchoolID) references School(SchoolID)
                foreign key(TeacherID) references Teacher(TeacherID)
                foreign key(StudentAbilityID) references StudentAbility(StudentAbilityID))"""
    create_table(db_name,"Student", sql)

def create_student_ability_table():
    sql = """create table StudentAbility
                (StudentAbilityID integer,
                StudentAbilityDescription text,
                primary key(StudentAbilityID))"""
    create_table(db_name,"Student Ability", sql)

def create_teacher_table():
    sql = """create table Teacher
                (TeacherID integer,
                SchoolID integer,
                TeacherName text,
                primary key(TeacherID)
                foreign key(SchoolID) references School(SchoolID))"""
    create_table(db_name,"Teacher", sql)

def create_school_table():
    sql = """create table School
                (SchoolID integer,
                SchoolName text,
                primary key(SchoolID))"""
    create_table(db_name,"School", sql)

if __name__ == "__main__":
    db_name = "Primary Maths Game.db"
    create_game_table()
    create_game_difficulty_table()
    create_attempt_table()
    create_student_table()
    create_student_ability_table()
    create_teacher_table()
    create_school_table()
