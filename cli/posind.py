'''position index value using deque and occurances'''
from collections import deque
d = deque([10,20,30,40,50])
v= int(input("Enter value to search: "))
if v in d:
    print("Index:", d.index(v))
else:
    print("not Found  !!!")
print("count:", d.count(v))
