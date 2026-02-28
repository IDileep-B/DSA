# write a code to demonstarte stack operations
stack= []
stack.append(10)
stack.append(11)
stack.append(55)
stack.append(22)
stack.append(12)
print("Stack after pushing: ", stack)
deleted = stack.pop()
print("Stack after popping 1 time : ", stack)
deleted = stack.pop()
print("Stack after popping 2 times : ", stack)

print("Stack element ready to be popped : ", stack[-1])
print("Remaining Size of the stack :", len(stack))