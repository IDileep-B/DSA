#insert a value in queue at rear using dequeu
from collections import deque
d= deque()
value= int(input("Enter value to inset: "))
d.append(value)
print("Dequed value insertion of ", d)