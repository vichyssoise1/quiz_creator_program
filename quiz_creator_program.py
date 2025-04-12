#!/usr/bin/env python3
# quiz_creator.py

import json

def main():
    filename = "questions.txt"
    with open(filename, "a", encoding="utf-8") as f:
        while True:
            question = input("Enter your question: ").strip()
            options = {}
            for opt in ["a", "b", "c", "d"]:
                options[opt] = input(f"Option {opt}: ").strip()
            
            # For now, just ask for an answer placeholder
            answer = input("Correct answer (a/b/c/d): ").strip().lower()

            # Build record and write
            record = {
                "question": question,
                "options": options,
                "answer": answer
            }
            f.write(json.dumps(record, ensure_ascii=False) + "\n")
            print("✔ Saved to questions.txt\n")

if __name__ == "__main__":
    main()
