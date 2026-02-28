'''code to illustrate queue operations using class
 insert an element from rear'''
class Queue:
    def __init__(self):
        self.queue= []
    def enqueue(self,value):
        self.queue.append(value)
        print(value,"Inserted")
q= Queue()
val= int(input("Enter a value to insert : "))
q.enqueue(val)
print("queued element :", q.queue)