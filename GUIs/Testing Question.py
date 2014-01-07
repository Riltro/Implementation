import random

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

Divison_Question = DivisionOne / DivisionTwo
while int(Division_Question) != Division_Question and DivisonOne > DisionTwo:
    Divison_Question = DivisonOne / DivisionTwo
Questions.append(Division_Question)

print(Question)
