from data import question_data
from ui import QuizInterface
from question_model import Question
from quiz_brain import QuizBrain

question_bank =[]
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question =Question(question_text,question_answer)
    question_bank.append(new_question)
    print(new_question.text,new_question.answer)
print(question_bank)

quiz_brain = QuizBrain(question_bank)
ui = QuizInterface(quiz_brain)