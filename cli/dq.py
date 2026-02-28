'''code to illustrate queue operations using class
 delete an element from front'''
class Queue:
    def __init__(self):
        self.queue= [10,20,30]
    def dequeue(self):
        if len(self.queue)==0:
            print("Queue Empty !!!")
        else:
            deleted= self.queue.pop(0)
            print(deleted, "Removed from queue")
q= Queue()
print("Queue befor delete:", q.queue)
q.dequeue()
print("Queue after delete:", q.queue)

