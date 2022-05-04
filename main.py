from data import question_data
from question_model import Question
from quiz import Quiz

question_bank = []



for q in question_data:
    question_text = q["question"]
    question_answer = q["question"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = Quiz(question_bank)

while quiz.remaining_questions():
    quiz.next_question()
print("All question have been answered !")
quiz_total = quiz.score / quiz.question_number
print(f"Your final score: {quiz_total}")