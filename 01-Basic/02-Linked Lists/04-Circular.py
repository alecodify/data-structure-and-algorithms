class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            new_node.next = self.head
            self.head = new_node
            current.next = self.head

    def delete(self, key):
        if self.head:
            if self.head.data == key:
                current = self.head
                while current.next != self.head:
                    current = current.next
                if self.head == self.head.next:
                    self.head = None
                else:
                    current.next = self.head.next
                    self.head = self.head.next
            else:
                current = self.head
                prev = None
                while current.next != self.head:
                    prev = current
                    current = current.next
                    if current.data == key:
                        prev.next = current.next
                        current = current.next
                        return
                if current.data == key:
                    prev.next = current.next

    def print_list(self):
        current = self.head
        if self.head:
            while True:
                print(current.data, end=" -> ")
                current = current.next
                if current == self.head:
                    break
            print()


cll = CircularLinkedList()
cll.append(1)
cll.append(2)
cll.append(3)
cll.prepend(0)
cll.print_list()

cll.delete(2)
cll.print_list()
