# quiz_creator.py

def main():
    while True:
        # 1) Ask for the question
        question = input("Enter your question: ").strip()
        
        # 2) Ask for four options
        options = {}
        for opt in ["a", "b", "c", "d"]:
            options[opt] = input(f"Option {opt}: ").strip()
        
        # 3) Echo back for now
        print("\nCollected:")
        print(f"  Q: {question}")
        for k, v in options.items():
            print(f"   {k}) {v}")
        print("-" * 40, "\n")

        # (Loop forever for now; exit logic comes later)

if __name__ == "__main__":
    main()
