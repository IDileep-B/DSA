# counting characters in a string
def count_char(text):
    count = 0
    for char in text:
        count += 1
    return count
 
def main():
   text = input("Enter name: ")
   print("char_count:",count_char(text))
main()
