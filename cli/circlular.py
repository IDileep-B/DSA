# write a cide to print the next biggest number of each element circular
stack= []
arr= list(map(int,input("enter numbers: ").split()))
n= len(arr)
result= [-1] *n

for i in range(2*n-1, -1, -1):
    while stack and stack[-1]<arr[i%n]:
        stack.pop()
        if i<n:
            if stack:
                result[i]= stack[-1]
        stack.append(arr[i%n])
print(result)
        
        