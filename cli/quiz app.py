# quiz app CLI

questions = [
    {"question": "2+2?", "answer": "4"},
    {"question": "Capital of India", "answer": "Delhi"}
]

# function to save score to file
def save_score(name, score):
    with open("scoreboard.txt", "a") as file:
        file.write(name + "-" + str(score) + "\n")

# function to display scorecard
def show_scoreboard():
    try:
        with open("scoreboard.txt", "r") as file:
            print("------ Scoreboard ------")
            print(file.read())
    except FileNotFoundError:
        print("No scores yet.")

# function to run quiz
def run_quiz():
    name = input("Enter your name: ")
    score = 0

    for q in questions:
        print(q["question"])
        answer = input("Your answer: ")

        if answer.lower() == q["answer"].lower():
            print("Correct!")
            score += 1
        else:
            print("Wrong! Correct answer is:", q["answer"])

    print("Your score:", score)
    save_score(name, score)

# main menu
def main():
    print("\n--- Quiz App Menu ---")
    print("1. Start Quiz")
    print("2. View Scoreboard")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        run_quiz()
    elif choice == "2":
        show_scoreboard()
    elif choice == "3":
        print("Exiting quiz app...")
        
    else:
        print("Invalid choice. Try again.")
main()