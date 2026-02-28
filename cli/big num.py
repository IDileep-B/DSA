# write a code to print the next biggest number of each element left
stack= []
arr= list(map(int, input("Enter numbers:").split()))
n= len(arr)
result= [-1] *n
for i in range(n):
    while stack and stack[-1]<=arr[i]:
        stack.pop()
        if stack:
            result[i]= stack[-1]
        stack.append(arr[i])
print(result)