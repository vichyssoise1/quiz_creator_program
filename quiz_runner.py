#!/usr/bin/env python3
# quiz_runner.py

import json
import random
from colorama import init, Fore
from pyfiglet import figlet_format
from inputimeout import inputimeout, TimeoutOccurred

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

    banner = figlet_format("Quiz Time!", font="slant")
    print(Fore.BLUE + banner)
    print(Fore.MAGENTA + "Type 'exit' anytime to quit.\n")

    questions = load_questions()
    if not questions:
        print(Fore.RED + "❌ No questions found.")
        return

    used = set()
    while True:
        if len(used) == len(questions):
            print(Fore.CYAN + "\n🎉 You've answered all available questions!")
            break

        question = random.choice(questions)
        while id(question) in used:
            question = random.choice(questions)
        used.add(id(question))

        print(Fore.CYAN + "\n🧠 " + question["question"])
        for key, value in question["options"].items():
            print(Fore.YELLOW + f"  {key}) {value}")
        
        try:
            answer = inputimeout(prompt=Fore.MAGENTA + "⏱️ Your answer (10s): ", timeout=10).strip().lower()
        except TimeoutOccurred:
            answer = None
            print(Fore.RED + "\n⏰ Time's up!")

        if answer == "exit":
            print(Fore.CYAN + "\n👋 Goodbye!")
            break
        elif answer is None:
            print(Fore.RED + f"❌ No answer given. Correct answer: {question['answer']}) {question['options'][question['answer']]}")
        elif answer == question["answer"]:
            print(Fore.GREEN + "✅ Correct!")
        else:
            correct_answer = question["options"][question["answer"]]
            print(Fore.RED + f"❌ Wrong. Correct answer: {question['answer']}) {correct_answer}")

if __name__ == "__main__":
    main()
