class QuizBrain:
    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0
        self.score=0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer=input(f"Q{self.question_number}- {current_question.question} (True/False):")
        self.check_answer(user_answer, current_question.answer)
        print(f"Your current score is {self.score}/{self.question_number} \n")



    def check_answer(self,user_answer,correct_answer):
        if user_answer.lower()==correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("You got it wrong!")

        print(f"The correct answer is {correct_answer}")
    def still_has_question(self):
        if self.question_number<len(self.question_list):
            return True
        else:
            print("You've completed all your quiz!")
            print(f"Your final score is {self.score}/{self.question_number}")
            return False


