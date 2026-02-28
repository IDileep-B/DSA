def star_pattern(n):
    for i in range(n):
        for j in range(n):
            if j >= i:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()

def main():
    n = int(input("Enter the number: "))
    star_pattern(n)

main()
      

