# counting vowels in string

def count_vowels(text):
    count = 0
    vowels = 'aeiouAEIOU'
    for char in text:
        if char in vowels:
            count += 1
    return count
def main():
    text = input("Enter name: ")
    print("vowels count:", count_vowels(text))
main()