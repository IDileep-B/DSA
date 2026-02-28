
def calculate_fee(course, marks):
    course = course.strip().lower()
    fees = {"ai": 40000, "web": 45000, "ds": 50000}
    fee = fees.get(course)
    if fee is None:
        return None

    if marks > 90:
        print("Discount applied: 5000")
        fee -= 5000

    return fee


def main():
    print("Student Fee Calculator")
    course = input("Enter course (AI/Web/DS): ")
    try:
        marks = int(input("Enter marks (0-100): "))
    except ValueError:
        print("Invalid marks. Please enter an integer from 0 to 100.")
        return

    if marks < 0 or marks > 100:
        print("Invalid marks. Please enter from 0 - 100.")
        return

    fee = calculate_fee(course, marks)
    if fee is None:
        print("Unknown course.")
    else:
        print(f"Final fee: {fee}")


if __name__ == "__main__":
    main()



    