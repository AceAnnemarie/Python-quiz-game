# Quiz Game

A simple command-line quiz game implemented in Python. The game presents trivia questions to the user and provides feedback based on their answers.

## Features

- Presents multiple-choice trivia questions.
- Tracks the user's score.
- Provides feedback on performance.

## Requirements

- Python 3.x

## Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/quiz-game.git
   cd quiz-game
   ```

2. **Run the Quiz Game**

   Execute the main game script:

   ```bash
   python quiz_game.py
   ```

## Script

### `quiz_game.py`

The main script that runs the quiz game. It uses hardcoded questions and answers to quiz the user. The script includes:

- A list of trivia questions with multiple-choice answers.
- Functions to display questions, validate answers, and track the user's score.
- Feedback on the user's performance at the end of the quiz.

### Code Overview

1. **`QUIZ_DATA`**: A list of dictionaries where each dictionary represents a quiz question, its choices, and the correct answer.

2. **`ask_question(question, choices, correct_answer)`**: Displays a question and its choices, then checks if the user's answer is correct.

3. **`main()`**: Manages the quiz flow, keeps track of the score, and provides feedback based on the user's performance.

## Customizing the Game

1. **Add New Questions**: To add new questions, modify the `QUIZ_DATA` list in the script. Each question is a dictionary with `question`, `choices`, and `correct` keys.

2. **Change Question Format**: Modify the `ask_question` function to adjust how questions and choices are presented.

## Example Usage

When you run the script, it will prompt you with multiple-choice questions. Type the number corresponding to your answer, and after answering all questions, it will display your final score and feedback.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Inspired by classic quiz games and educational tools.
