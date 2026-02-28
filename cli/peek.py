'''code to illustrate queue operations using class
peek an element from front and print the size of queue'''
class Queue:
    def __init__(self):
        self.queue= [10,20,30]
    def peek(self):
        if len(self.queue)==0:
            print("Queue Empty !!!")
        else:
            print("Front element ", self.queue[0])
            print("Size of queue",len(self.queue))
q= Queue()
q.peek()    