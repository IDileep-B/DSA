# write a code to manipulate a stack to monotonic decreasing stack
stack=[]
arr=list(map(int,input("enter the numbers :").split()))
for i in arr:
    while stack and stack[-1]>i:
        stack.pop()
    stack.append(i)
print("monotonic decreasing stack:",stack)