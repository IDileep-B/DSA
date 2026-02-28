# write a code to check an expression to balance
exp= input("Enter an expression: ")
stack= []
for ch in exp:
    if ch in '({[':
        stack.append(ch)
    elif ch in ')}]' :
        if not stack:
            print("Expression is not balanced.")
            break
        top = stack.pop()
        if (ch == ")" and top != "(") or \
           (ch == "}" and top != "{") or \
           (ch == "]" and top != "["):
            print("Expression is not balanced.")
            break
else:
    if not stack:
        print("Expression is balanced.")
    else:
        print("Expression is not balanced.")