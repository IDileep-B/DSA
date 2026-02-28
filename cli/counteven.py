# counting even numbers from 1 to n

from gc import get_count
import numbers


def count_odd(n):
    count = 0
    for i in range(1, n+1):
        if i % 2 == 0:
            count += 1
    return count

def main():
    n = int(input("Enter a number: "))
    odd_count = count_odd(n)
    print("odd count:", count_odd(n))
main() 







# counting positive numbers
def count_positive(numbers):
    count = 0
    for num in numbers:
        if num > 0:
            count += 1
    return count

def main():
    numbers = [1, -2, 3, 4, -5, 6]
    print("positive numbers count:", count_positive(numbers))
main()