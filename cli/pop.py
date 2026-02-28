from collections import deque
d = deque([10,20,30,40,50])
print("Dequed ",d)
removed = d.pop()
print("Removed element ", removed)
print("Dequed", d)
left_removed = d.popleft()
print("Left removed element ", left_removed)
print("Dequed", d)