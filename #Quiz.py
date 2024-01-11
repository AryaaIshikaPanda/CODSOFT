#Quiz
import random

def load_quiz_questions():
    # Define your quiz questions and answers
    questions = ["Question 1?", "Question 2?", "Question 3?"]
    choices = [["Option A", "Option B", "Option C"],
               ["Option X", "Option Y", "Option Z"],
               ["Option P", "Option Q", "Option R"]]
    correct_answers = [1, 2, 0]  # Index of correct choices for each question
    return questions, choices, correct_answers

def display_welcome_message():
    print("Welcome to the Quiz Game!")
    print("Answer the following questions and test your knowledge.")

def present_quiz_questions(questions, choices):
    for i in range(len(questions)):
        print(f"\n{questions[i]}")
        for j, choice in enumerate(choices[i]):
            print(f"{j + 1}. {choice}")

def evaluate_user_answer(user_answer, correct_answer, score):
    if user_answer == correct_answer:
        print("Correct!")
        score += 1
    else:
        print(f"Incorrect. The correct answer is {correct_answer + 1}.")
    return score

def display_final_results(score, total_questions):
    print(f"\nYour final score is {score}/{total_questions}.")
    if score == total_questions:
        print("Congratulations! You got all the questions right.")
    elif score >= total_questions // 2:
        print("Good job! You did well.")
    else:
        print("Keep practicing. You can do better next time.")

def play_quiz_game():
    questions, choices, correct_answers = load_quiz_questions()
    total_questions = len(questions)
    score = 0

    display_welcome_message()

    while questions:
        random_index = random.randint(0, len(questions) - 1)
        current_question = questions.pop(random_index)
        current_choices = choices.pop(random_index)
        correct_answer = correct_answers.pop(random_index)

        present_quiz_questions([current_question], [current_choices])
        user_answer = int(input("Enter your choice (1, 2, or 3): "))
        score = evaluate_user_answer(user_answer - 1, correct_answer, score)

    display_final_results(score, total_questions)

play_quiz_game()