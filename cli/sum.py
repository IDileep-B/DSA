# write a code to print sum of first n numbers

def calculate_sum(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

def main():
    n = int(input("Enter a number: "))
    result = calculate_sum(n)
    print("Sum of numbers up to", n, "is", result)

if __name__ == "__main__":
    main()
