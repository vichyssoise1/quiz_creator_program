#!/usr/bin/env python3
# quiz_runner.py

import json
import random

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
    questions = load_questions()
    if not questions:
        print("❌ No questions found.")
        return

    question = random.choice(questions)
    print("\n🧠 " + question["question"])
    for key, value in question["options"].items():
        print(f"  {key}) {value}")
    
    answer = input("Your answer (a/b/c/d): ").strip().lower()
    if answer == question["answer"]:
        print("✅ Correct!")
    else:
        correct_answer = question["options"][question["answer"]]
        print(f"❌ Wrong. Correct answer: {question['answer']}) {correct_answer}")

if __name__ == "__main__":
    main()
