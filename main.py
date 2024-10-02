from question_model import Question
from quiz_brain import QuizBrain
from data import question_data

question_bank = []

for question in question_data:
    qanda = Question(f"{question['question']}", f"{question['correct_answer']}")
    question_bank.append(qanda)
    #question_text = question["text"]
    #question_answer = question["answer"]
    #new_question = Question(question_text, question_answer)
    #question_bank.append(new_question)
print(question_bank)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
    
print("You've completed the quiz")
print(f"Your final answer is {quiz.score}/{len(question_bank)}")