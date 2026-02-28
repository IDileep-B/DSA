def run_quiz(questions):
    score = 0
    for q in questions:
        print("\n" + q["question"])
        for option in q["options"]:
            print(option)
        answer = input("Your answer: ").strip().upper()
        if answer == q["answer"]:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer was {q['answer']}")
    print(f"\nYour final score: {score}/{len(questions)}")

quiz_questions = [
    {
        "question": "What is the output of print(2 ** 3)?",
        "options": ["A. 6", "B. 8", "C. 9", "D. 5"],
        "answer": "B"
    },
    {
        "question": "Which of these is a mutable data type in Python?",
        "options": ["A. Tuple", "B. String", "C. List", "D. Frozenset"],
        "answer": "C"
    },
    {
        "question": "What keyword is used to define a function in Python?",
        "options": ["A. func", "B. def", "C. function", "D. lambda"],
        "answer": "B"
    }
]

run_quiz(quiz_questions)
