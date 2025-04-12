#!/usr/bin/env python3
# quiz_creator.py

import json

def main():
    filename = "questions.txt"
    with open(filename, "a", encoding="utf-8") as f:
        while True:
            question = input("Enter your question (or type 'exit'): ").strip()
            if question.lower() == "exit":
                print("Exiting. All done!")
                break

            options = {}
            for opt in ["a", "b", "c", "d"]:
                options[opt] = input(f"Option {opt}: ").strip()

            answer = ""
            while answer not in options:
                answer = input("Correct answer (a/b/c/d): ").strip().lower()
                if answer not in options:
                    print("  → Invalid, choose a/b/c/d.")

            record = {
                "question": question,
                "options": options,
                "answer": answer
            }
            f.write(json.dumps(record, ensure_ascii=False) + "\n")
            print("✔ Saved!\n")

if __name__ == "__main__":
    main()
