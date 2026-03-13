from phonebook import phonebook

def add_contact():
    name = input("Enter name: ")
    number = input("Enter number: ")

    phonebook[name] = 