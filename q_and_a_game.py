"""This program is a multiple options quiz."""


list_of_questions = [
    {"prompt": "1. What is the capital of France?",
     "options": ["A. Madrid", "B. Rome", "C. Paris",
                 "D. Berlin", "E. Lisbon"],
     "answer": "C"
     },
    {"prompt": "2. Which planet is known as the Red Planet?",
     "options": ["A. venus", "B. Mars", "C. Jupiter",
                 "D. Saturn", "E. Mercury"],
     "answer": "B"
     },
    {"prompt": "3. What is the largest organ in the human body?",
     "options": ["A. Brain", "B. Heart", "C. Skin",
                 "D. Liver", "E. Stomach"],
     "answer": "C"
     },
    {"prompt": "4. Who wrote Hamlet?",
     "options": ["A. Charles Dickens", "B. William Shakespeare", "C. J.K. \
                 Rowling", "D. Mark Twain", "E. George Orwell"],
     "answer": "B"
     },
    {"prompt": "5. What is the chemical symbol for Gold?",
     "options": ["A. Ag", "B. Au", "C. Pb", "D. Fe", "E. Hg"],
     "answer": "B"
     },
    {"prompt": "6. How many continents are there on Earth?",
     "options": ["A. 5", "B. 6", "C. 7", "D. 8", "E. 4"],
     "answer": "C"
     },
    {"prompt": "7. Which gas do plants absorb from the atmosphere?",
     "options": ["A. Oxygen", "B. Carbon Dioxide", "C. Nitrogen",
                 "D. Hydrogen", "E. Methane"],
     "answer": "B"
     },
    {"prompt": "8. Who painted the Mona Lisa?",
     "options": ["A. Pablo Picasso", "B. Vincent van Gogh", "C. Leonard \
                 da vinci", "D. Caude Monet", "E. Michelangelo"],
     "answer": "C"
     },
    {"prompt": "9. What is the square root of 64?",
     "options": ["A. 6", "B. 7", "C. 8", "D. 9", "E. 10"],
     "answer": "C"
     },
    {"prompt": "10. Which ocean is the largest?",
     "options": ["A. Atlantic Ocean", "B. Indian Ocean", "C. Artic Ocean",
                 "D. Pacific Ocean", "E. Southern Ocean"],
     "answer": "D"
     }
]


def run_quiz(questions):
    """Return the right answer to a question.

    Args:
        questions (list): a list of predefined questions and answers.

    Returns:
        string: the correct answer to a question.
    """
    score = 0
    for question in questions:
        print(question["prompt"])
        for option in question["options"]:
            print(option)
        answer = input("Enter your answer (A, B, C, D, E): ").upper()
        if answer == question["answer"]:
            score += 1
            print("\nCorrect, hurray!\n")
        else:
            print(f'\nWrong!!! The correct answer was {question["answer"]}!\n')
    print(f"Your total score is {score}")


run_quiz(list_of_questions)
