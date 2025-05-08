#!/usr/bin/env python3
# quiz_runner.py

import json
import random
from colorama import init, Fore, Style

def load_questions(filename="questions.txt"):
    questions = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            try:
                questions.append(json.loads(line))
            except json.JSONDecodeError:
                continue
    return questions

def main():
    init(autoreset=True)
    questions = load_questions()
    if not questions:
        print(Fore.RED + "❌ No questions found.")
        return

    question = random.choice(questions)
    print(Fore.CYAN + "\n🧠 " + question["question"])
    for key, value in question["options"].items():
        print(Fore.YELLOW + f"  {key}) {value}")
    
    answer = input(Fore.MAGENTA + "Your answer (a/b/c/d): ").strip().lower()
    if answer == question["answer"]:
        print(Fore.GREEN + "✅ Correct!")
    else:
        correct_answer = question["options"][question["answer"]]
        print(Fore.RED + f"❌ Wrong. Correct answer: {question['answer']}) {correct_answer}")

if __name__ == "__main__":
    main()
