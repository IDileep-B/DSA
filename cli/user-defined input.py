# write a code to take user-defined input to create a stack
stack=[]
n= int(input("enter the size of stack :"))
for i in range(n):
    value = int(input("enter a value :"))
    stack.append(value)
print("stack:",stack)
print("pop :", stack.pop())
print("stack:",stack)
