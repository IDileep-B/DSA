''' write a code to reverse a string using a stack'''
text= input("Enter a string: ")
stack= []
for ch in text:
     stack.append(ch)
rev_string = ''
while stack:
    rev_string += stack.pop()
print("Reversed string:", rev_string)