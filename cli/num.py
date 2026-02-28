#  print numbers from 1 to N

def  print_numbers(n):
    for i in range(1, n+1):
        print(i)

def main():
    n = int(input("Enter a number :"))
    print_numbers(n)

if __name__ == "__main__":
    main()
                
