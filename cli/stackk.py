class stack:
    def __init__(self, size):
        self.stack = []
        self.size = size
        def is_full(self):
            return len(self.stack) == self.size
        def push(self, value):
            if self.is_full():
                print("stack overflow !!!!")
            else:
                self.stack.append(value)
                print(value,"pushed")
s: stack= stack(3)

