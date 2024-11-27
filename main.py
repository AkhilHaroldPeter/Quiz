from Question_Data import *
from Question_Modal import Question
from Quiz_Master import QuizMaster
from art import *
import random
import sys



No_of_question = input('Please select the number of questions you would like between 1-45 : ')
# to check if the user has typed a number between 1- 45
if not No_of_question.isdigit():
    sys.exit(f'incorrect value "{No_of_question}"')
elif No_of_question.isdigit() and (1 > int(No_of_question) or int(No_of_question) > 45):
    sys.exit(f'incorrect value "{No_of_question}". Please type a number between 1 to 45!')
else:
    No_of_question = int(No_of_question)
Question_Bank = []
for _ in range(No_of_question):
    # To pick a random set of question from "question_data" list
    Random_Question_Generator = random.choice(question_data)
    # to assign the above extracted value of question in "Question"
    Selected_Question = Random_Question_Generator['question']
    # to assign the above extracted value of answer in "Answer"
    Selected_Answer = Random_Question_Generator['correct_answer']
    # Creating a new
    New_Question = Question(Selected_Question, Selected_Answer)
    Question_Bank.append(New_Question)

Quiz = QuizMaster(Question_Bank)

while Quiz.questions_remaining():
    Quiz.next_question()

print("You've completed the quiz")
print(f'Your final score : {Quiz.score}/{Quiz.Question_Number}')
print(text2art('Game Over', font='small'))
