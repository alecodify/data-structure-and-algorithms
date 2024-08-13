"""
Queue follows the First In First Out (FIFO) rule. 
the item that goes in first is the item that comes out first.
"""

class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, item):
        self.queue.append(item)
        print(f"enqueue item: {item} ")
    
    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)
    
    def display(self):
        print(self.queue)
    
    def size(self):
        return len(self.queue)
    

q = Queue()
q.enqueue(1)    
q.enqueue(2)    
q.enqueue(3)    
q.enqueue(4)    
q.enqueue(5)

q.display()  

print(f"dequeue the item: {q.dequeue()}")  
q.display()

q.enqueue(6)
q.display()

print(f"dequeue the item: {q.dequeue()}") 
q.display() 