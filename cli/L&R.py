# rotate left and right
from collections import deque
d= deque([11,22,33,44,55])
d.rotate(2)
print("Right rotate", d)
d.rotate(-2)
print("left rotate 2 times", d)