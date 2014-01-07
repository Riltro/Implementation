import random

def QuestionGenerator():

    AdditionOne = random.randint(1,20)
    AdditionTwo = random.randint(1,20)
    SubtractionOne = random.randint(1,20)
    SubtractionTwo = random.randint(1,20)
    MultiplicationOne = random.randint(1,12)
    MultiplicationTwo = random.randint(1,12)
    DivisionOne = random.randint(1,12)
    DivisonTwo = random.randint(1,12)
    
    Questions = []

    Addition_Question = AdditionOne + AdditionTwo
    Questions.append(Addition_Question)
    
    Svalid = False
    while Svalid == False:
        Subtraction_Question = SubtractionOne - SubtractionTwo
        if SubtractionTwo > SubtractionOne:
            Svalid = False
        elif SubtractionOne > SubtractionTwo:
            Svalid = True
    Questions.append(Subtraction_Question)

    Multiplication_Question = MultiplicationOne * MultiplicationTwo
    Questions.append(Multiplication_Question)

    Divison_Question = ""
    while int(Division_Question) != Division_Question and DivisonOne > DisionTwo:
        Divison_Question = DivisonOne / DivisionTwo
    Questions.append(Division_Question)

    print(Addition_Question)
    print(Subtraction_Question)
    print(Multiplication_Question)
    print(Divison_Question)

    return Questions

def get_question():
    selection_number = random.randint(0,3)
    Question_List = QuestionGenerator()
    Selected_Question = Question_List[selection_number]
    return Selected_Question

def main():
    QuestionGenerator()
    Selected_Question = get_question(Questions)
    
    
    
    
    
