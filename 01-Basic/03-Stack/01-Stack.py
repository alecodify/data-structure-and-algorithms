"""
A stack is a linear data structure that follows the principle of Last In First Out (LIFO). 
This means the last element inserted inside the stack is removed first.
"""

class Stack:
    def __init__(self):
        self.stack = []
    
    def check_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)
        print("pushed item: " + item)
    
    def pop(self):
        if self.check_empty():
            return "stack is empty"

        return self.stack.pop()
    
    def display(self):
        return str(self.stack)    
    

stack = Stack()
stack.push(str(1))
stack.push(str(2))
stack.push(str(3))

print("pop item: " + stack.pop())
print("stack after popping an element: " + stack.display())