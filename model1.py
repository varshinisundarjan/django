# simple_quiz.py

class Question:
    def __init__(self, question_text, choices, correct_choice):
        self.question_text = question_text
        self.choices = choices  # list of choices
        self.correct_choice = correct_choice  # index of correct choice (0-based)

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.submissions = []

    def start(self):
        print("Welcome to the Quiz!\n")
        for i, question in enumerate(self.questions, start=1):
            print(f"Q{i}: {question.question_text}")
            for idx, choice in enumerate(question.choices, start=1):
                print(f"{idx}. {choice}")
            while True:
                try:
                    answer = int(input("Enter your choice number: "))
                    if 1 <= answer <= len(question.choices):
                        break
                    else:
                        print(f"Please enter a number between 1 and {len(question.choices)}")
                except ValueError:
                    print("Invalid input. Enter a number.")
            
            self.submissions.append((question.question_text, question.choices[answer-1]))
            if answer-1 == question.correct_choice:
                self.score += 1
            print()

        self.show_result()

    def show_result(self):
        print("\n--- Quiz Result ---")
        print(f"Your Score: {self.score}/{len(self.questions)}\n")
        print("Your Submissions:")
        for q, ans in self.submissions:
            print(f"Question: {q}")
            print(f"Your Answer: {ans}")
            print("-"*30)

# Example Questions
questions_list = [
    Question("What is the capital of France?", ["Paris", "London", "Berlin", "Rome"], 0),
    Question("2 + 2 = ?", ["3", "4", "5", "6"], 1),
    Question("Which language is this code written in?", ["Java", "Python", "C++", "JavaScript"], 1),
]

# Start Quiz
quiz = Quiz(questions_list)
quiz.start()
