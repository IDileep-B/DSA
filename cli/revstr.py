# reverse a string
def rev_str(text):
    reversed_text = ""
    for char in text:
        reversed_text = char + reversed_text
    return reversed_text
def main():
    text = input("Enter name: ")
    print("Reversed text: " , rev_str(text))
main()
