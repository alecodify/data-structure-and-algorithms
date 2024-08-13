"""
Deque or Double Ended Queue is a type of queue in which insertion and removal of elements can either be performed from the front or the rear.
Thus, it does not follow FIFO rule (First In First Out).
"""

class Deque:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []

    def addRear(self, item):
        self.items.append(item) # add element to rear (end) of queue
    
    def addFront(self, item):
        self.items.insert(0, item) # add element to front (beginning) of queue
    
    def removeRear(self):
        return self.items.pop() # remove element from the end
    
    def removeFront(self):
        return self.items.pop(0) # remove element from beginning    
    
    def size(self):
        return len(self.items)

d = Deque()

print(d.isEmpty())

d.addRear(8) # Deque: [8]
d.addRear(5) # Deque: [8, 5]
d.addFront(7) # Deque: [7 ,8, 5]
d.addFront(10) # Deque: [10, 7, 8, 5]
d.addRear(11) # Deque: [10, 7, 8, 5, 11]

print(d.size())
print(d.removeRear()) # Deque after removal: [10, 7, 8, 5]
print(d.removeFront()) # Deque after removal: [7, 8, 5]

print(d.items) # output: [7, 8, 5] 