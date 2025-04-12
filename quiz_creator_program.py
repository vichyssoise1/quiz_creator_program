#!/usr/bin/env python3
# quiz_creator.py

import json
from colorama import init, Fore, Style

def main():
    init(autoreset=True)
    filename = "questions.txt"
    print(Fore.MAGENTA + f"Questions will be saved to {filename}\n")

    with open(filename, "a", encoding="utf-8") as f:
        while True:
            print(Fore.YELLOW + "Enter your question (or type 'exit'):")
            question = input("> ").strip()
            if question.lower() == "exit":
                print(Fore.CYAN + "Exiting. All done!")
                break

            options = {}
            for opt in ["a", "b", "c", "d"]:
                print(Fore.YELLOW + f"Option {opt}:", end=" ")
                options[opt] = input().strip()

            answer = ""
            while answer not in options:
                print(Fore.YELLOW + "Correct answer (a/b/c/d):", end=" ")
                answer = input().strip().lower()
                if answer not in options:
                    print(Fore.RED + "  → Invalid, choose a/b/c/d.")

            record = {"question": question, "options": options, "answer": answer}
            f.write(json.dumps(record, ensure_ascii=False) + "\n")
            print(Fore.GREEN + "✔ Saved!\n")

if __name__ == "__main__":
    main()
