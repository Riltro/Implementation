import random


FirstNumberList = []
for each in range(20):
    FirstNumber = random.randint(1,20)
    FirstNumberList.append(FirstNumber)

SecondNumberList = []
for each in range(20):
    SecondNumber = random.randint(1,20)
    SecondNumberList.append(SecondNumber)

SignList = []
SignList.append("*")
SignList.append("-")
SignList.append("+")
SignList.append("/")

ListChoice = random.randint(0,19)
SignListChoice = random.randint(0,3)

QuestionList = []

for each in range(20):
    ListChoice = random.randint(0,19)
    SignListChoice = random.randint(0,3)
    Question = str(FirstNumberList[ListChoice]),str(SignList[SignListChoice]),str(SecondNumberList[ListChoice])
    NewQuestion = ("".join(map(str,Question)))

    QuestionList.append(NewQuestion)

for count in range(len(QuestionList)):
    print(count+1,QuestionList[count])



