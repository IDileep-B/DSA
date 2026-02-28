# write a code to perform stack empty in  a stack

class stack:
    def __init__(self):
        self.stack=[]
    def is_empty(self):
        return len(self.stack) ==0
    def pop(self):
        if self.is_empty():
            print("stack empty !!!!")
        else:
            print("popped:",self.stack.pop())
s= stack()
s.pop()