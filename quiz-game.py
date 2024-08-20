import sys

# List of questions, each with a list of answer choices and the correct answer
QUIZ_DATA = [
    {
        "question": "What is the capital of France?",
        "choices": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
        "correct": "C"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "choices": ["A. Earth", "B. Jupiter", "C. Mars", "D. Venus"],
        "correct": "C"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "choices": ["A. Atlantic Ocean", "B. Indian Ocean", "C. Arctic Ocean", "D. Pacific Ocean"],
        "correct": "D"
    },
    {
        "question": "Who wrote 'To Kill a Mockingbird'?",
        "choices": ["A. Harper Lee", "B. Mark Twain", "C. J.K. Rowling", "D. Ernest Hemingway"],
        "correct": "A"
    },
    {
        "question": "What is the chemical symbol for gold?",
        "choices": ["A. Au", "B. Ag", "C. Pb", "D. Fe"],
        "correct": "A"
    }
]

def ask_question(question, choices, correct_answer):
    """
    Asks a single question and checks if the provided answer is correct.

    Args:
    question (str): The question to be asked.
    choices (list): A list of answer choices.
    correct_answer (str): The correct answer's choice letter.

    Returns:
    bool: True if the answer is correct, False otherwise.
    """
    print(question)
    for choice in choices:
        print(choice)
    answer = input("Please enter the letter of your answer: ").strip().upper()
    return answer == correct_answer

def main():
    """
    Runs the quiz game, keeps track of score and provides feedback.
    """
    score = 0
    total_questions = len(QUIZ_DATA)
    
    print("Welcome to the Quiz Game!")
    print("Answer the following questions by typing the letter of your choice.\n")
    
    for question_data in QUIZ_DATA:
        question = question_data["question"]
        choices = question_data["choices"]
        correct = question_data["correct"]
        
        if ask_question(question, choices, correct):
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong. The correct answer was {correct}.\n")
    
    print(f"Quiz Over! Your final score is {score} out of {total_questions}.")
    
    if score == total_questions:
        print("Congratulations, you got a perfect score!")
    elif score > total_questions / 2:
        print("Good job! You did well.")
    else:
        print("Better luck next time!")

if __name__ == "__main__":
    main()
