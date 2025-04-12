#!/usr/bin/env python3
# quiz_creator.py

import json
from colorama import init, Fore
from pyfiglet import figlet_format

def main():
    init(autoreset=True)

    # Cool ASCII banner
    banner = figlet_format("Quiz Creator", font="slant")
    print(Fore.CYAN + banner)
    print(Fore.MAGENTA + "Your questions will be saved to questions.txt\n")

    with open("questions.txt", "a", encoding="utf-8") as f:
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
