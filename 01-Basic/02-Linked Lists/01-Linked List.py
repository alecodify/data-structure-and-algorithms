class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

""" Node Structure
    +----+------+ 
    | data | None ->  | 
    +----+------+ 
"""

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        
        last = self.head
        while last.next:
            last = last.next
        last.next =  new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

def main():
    lisked_list = LinkedList()

    lisked_list.insert(10)
    lisked_list.insert(20)
    lisked_list.insert(30)

    print(lisked_list.display())

""" Linked List Representation after insertions:
    +----+------+     +----+------+     +----+------+
    | 10 |  ->  | --> | 20 |  ->  | --> | 30 | None |
    +----+------+     +----+------+     +----+------+
"""

if __name__ == "__main__":
    main()