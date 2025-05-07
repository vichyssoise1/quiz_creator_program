#!/usr/bin/env python3
# quiz_runner.py

import json

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
    print(f"Loaded {len(questions)} questions.")
    # More to come...

if __name__ == "__main__":
    main()
