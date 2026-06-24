import json
from pathlib import Path

SCORES_FILE = Path("scores.json")
QUES_FILE = Path("questions.json")


def load_scores():
    if SCORES_FILE.exists():
        with open(SCORES_FILE, "r") as file:
            return json.load(file)
    return []


def save_scores(scores):
    with open(SCORES_FILE, "w") as file:
        json.dump(scores, file, indent=4)


def load_questions():
    if QUES_FILE.exists():
        with open(QUES_FILE, "r") as file:
            return json.load(file)
    return []


def start_quiz():
    questions = load_questions()
    scores = load_scores()

    if not questions:
        print("No questions found.")
        return

    score = 0

    for question in questions:
        print(f"\n{question['question']}")
        user_answer = input("Your answer: ").strip().lower()

        if user_answer == question["answer"].lower():
            score += 1
            print("Correct!")
        else:
            print("Incorrect!")

    result = {
        "score": score,
        "total": len(questions)
    }

    scores.append(result)
    save_scores(scores)

    print(f"\nQuiz Complete. Score: {score}/{len(questions)}")


def view_scores():
    scores = load_scores()

    if not scores:
        print("No previous scores found.")
        return

    for index, score in enumerate(scores, start=1):
        print(f"Quiz {index}: {score['score']}/{score['total']}")


def quiz_menu():
    print("""
===== Quiz App =====
1. Start Quiz
2. View Previous Scores
3. Exit
""")


def main():
    while True:
        quiz_menu()

        choice = input("Choose an option: ").strip()

        if choice == "1":
            start_quiz()

        elif choice == "2":
            view_scores()

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please choose between 1 and 3.")


main()