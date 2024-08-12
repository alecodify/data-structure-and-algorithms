class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
            self.head.prev = self.head
        else:
            tail = self.head.prev
            tail.next = new_node
            new_node.prev = tail
            new_node.next = self.head
            self.head.prev = new_node

    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
            self.head.prev = self.head
        else:
            tail = self.head.prev
            new_node.next = self.head
            new_node.prev = tail
            self.head.prev = new_node
            tail.next = new_node
            self.head = new_node

    def delete(self, key):
        if self.head:
            current = self.head
            while True:
                if current.data == key:
                    if current == self.head:
                        if self.head.next == self.head:
                            self.head = None
                        else:
                            tail = self.head.prev
                            self.head = self.head.next
                            tail.next = self.head
                            self.head.prev = tail
                    else:
                        current.prev.next = current.next
                        current.next.prev = current.prev
                    return
                current = current.next
                if current == self.head:
                    break

    def print_list(self):
        if self.head:
            current = self.head
            while True:
                print(current.data, end=" <-> ")
                current = current.next
                if current == self.head:
                    break
            print()


cdll = CircularDoublyLinkedList()
cdll.append(1)
cdll.append(2)
cdll.append(3)
cdll.prepend(0)
cdll.print_list()  

cdll.delete(2)
cdll.print_list()  

cdll.delete(0)
cdll.print_list() 
