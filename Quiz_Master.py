class QuizMaster:
    def __init__(self, question_list):
        self.Question_Number = 0
        self.Question_List = question_list
        self.score = 0

    def next_question(self):
        current_question = self.Question_List[self.Question_Number]
        self.Question_Number += 1
        user_answer = input(f'Q.{self.Question_Number}: {current_question.Question} (True/False): ')
        # print('-'*10)
        # print(current_question.Answer)
        self.verify_answer(user_answer, current_question.Answer)

    def questions_remaining(self):
        return self.Question_Number < len(self.Question_List)

    def verify_answer(self, user_answer, correct_answer):
        if str(user_answer).lower() == str(correct_answer).lower():
            self.score += 1
            print("You've nailed it!")
        else:
            print("That's incorrect.")
        print(f"The correct answer : {correct_answer}")
        print(f"You correct score is {self.score}/{self.Question_Number}.\n\n")



