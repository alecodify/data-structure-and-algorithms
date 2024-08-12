class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

""" Node Structure
    +----+------+----+ 
    | data | None -> | 
    +----+------+----+ 
"""
    
class SinglyLinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head =  new_node
            return
        
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
    
    def insert_at_index(self, data, index):
        if index < 0:
            print("Index out of bounds")
            return
        new_node = Node(data)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        
        current = self.head
        current_position = 0

        while current and current_position < index - 1:
            current = current.next
            current_position += 1
        
        if current is None:
            print("Index out of bounds")
            return

        new_node.next = current.next
        current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def delete_from_start(self):
        if not self.head:
            print("List is empty")
            return;
        deleted_node = self.head
        self.head = self.head.next
        print(f"Deleted element from start: {deleted_node.data}")

    def delete_from_end(self):
        if not self.head:
            print("List is empty")
            return
        if self.head.next is None:
            deleted_node = self.head
            self.head = None
            print(f"Deleted element from end: {deleted_node.data}")
            return

        second_last = self.head
        while second_last.next.next:
            second_last = second_last.next
        
        deleted_node = second_last.next
        second_last.next = None
        print(f"Deleted element from end: {deleted_node.data}")

    def delete_from_index(self, index):
        if index < 0:
            print("Index out of bounds")
            return
        if not self.head:
            print("List is empty")
            return
        if index == 0:
            self.delete_from_start()
            return

        current = self.head
        current_position = 0

        while current and current_position < index - 1:
            current = current.next
            current_position += 1

        if current is None or current.next is None:
            print("Index out of bounds")
            return

        deleted_node = current.next
        current.next = current.next.next
        print(f"Deleted element from index {index}: {deleted_node.data}") 

    def linear_search(self, key):
        current = self.head
        position = 0
        while current:
            if str(current.data) == str(key):
                print(f"Element {key} found at position {position}")
                return
            current = current.next
            position += 1
        print(f"Element {key} not found in the list")

    def binary_search(self, key):
        def to_list(node):
            lst = []
            while node:
                lst.append(int(node.data))
                node = node.next
            return lst
        
        self.sort()

        lst = to_list(self.head)
        print(f"sorted {lst}")

        low, high = 0, len(lst) - 1
        while low <= high:
            mid = (low + high) // 2
            if lst[mid] == key:
                print(f"Element {key} found at position {mid}")
                return
            elif lst[mid] < key:
                low = mid + 1
            else:
                high = mid - 1
        print(f"Element {key} not found in the list")

    def search_at_index(self, index):
        if index < 0:
            print("Index out of bounds")
            return
        current = self.head
        current_position = 0
        while current and current_position < index:
            current = current.next
            current_position += 1
        if current:
            print(f"Element at index {index} is {current.data}")
        else:
            print(f"Index {index} is out of bounds")
    

    def sort(self):
        if not self.head or not self.head.next:
            return

        end = None
        while end != self.head:
            current = self.head
            while current.next != end:
                next_node = current.next
                if int(current.data) > int(next_node.data):
                    current.data, next_node.data = next_node.data, current.data
                current = current.next
            end = current

def main():
    singly_linked_list = SinglyLinkedList()

    element = int(input("Enter the element in the linked list: "))
   
    singly_linked_list.insert_at_end(element)
    
    print("Initial Linked List: ")
    singly_linked_list.display()

    while True:
        print("\nChoose an option: ")
        print("1. Insertion")
        print("2. Deletion")
        print("3. Search")
        print("4. Sorting")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            while True:
                print("\nChoose an Insertion You want to Perform: ")
                print("1. Insert at the beginning")
                print("2. Insert at the end")
                print("3. Insert at a specific index")
                print("4. Back")

                insertion_choice = int(input("Enter your choice: "))

                if insertion_choice == 1:
                    element = input("Enter the element to insert at the beginning: ")
                    singly_linked_list.insert_at_beginning(element)
                    singly_linked_list.display()

                elif insertion_choice == 2:
                    element = input("Enter the element to insert at the end: ")
                    singly_linked_list.insert_at_end(element)
                    singly_linked_list.display()
                
                elif insertion_choice == 3:
                    element = input("Enter the element to insert: ")
                    index = int(input("Enter the index to insert at: "))
                    singly_linked_list.insert_at_index(element, index)
                    singly_linked_list.display()
                
                elif insertion_choice == 4:
                    break

                else:
                    print("Invalid choice, please try again.")

        elif choice == 2:
            while True:
                print("\nChoose an Deletion You want to Perform: ")
                print("1. Delete from the beginning")
                print("2. Delete from the end")
                print("3. Delete from a specific index")
                print("4. Back")

                deletion_choice = int(input("Enter your choice: "))

                if deletion_choice == 1:
                    singly_linked_list.delete_from_start()
                    singly_linked_list.display()
                
                elif deletion_choice == 2:
                    singly_linked_list.delete_from_end()
                    singly_linked_list.display()
                
                elif deletion_choice == 3:
                    index = int(input("Enter the index to delete from: "))
                    singly_linked_list.delete_from_index(index)
                    singly_linked_list.display()

                elif deletion_choice == 4:
                    break

                else:
                    print("Invalid choice, please try again.")  

        elif choice == 3:
            while True:
                print("\nChoose an Search method You want to Perform: ")
                print("1. Linear Search")
                print("2. Binary Search")
                print("3. Search at a specific index")
                print("4. Back")

                search_choice = int(input("Enter your choice: "))
                singly_linked_list.display()

                if search_choice == 1:
                    key = int(input("Enter the element to search: "))
                    singly_linked_list.linear_search(key)
                
                elif search_choice == 2:
                    key = int(input("Enter the element to search: "))
                    singly_linked_list.binary_search(key)

                elif search_choice == 3:
                    index = int(input("Enter the index to search: "))
                    singly_linked_list.search_at_index(index)
                
                elif search_choice == 4:
                    break

                else:
                    print("Invalid choice, please try again.")


        elif choice == 4:
            while True:
                print("\nChoose the below option: ")
                print("1. Sorting")
                print("2. Back")

                sorting_choice = int(input("Enter your choice: "))

                if sorting_choice == 1:
                    singly_linked_list.sort()
                    singly_linked_list.display()

                elif sorting_choice == 2:
                    break
                else:
                   print("Invalid choice, please try again.")  



        elif choice == 5:
            print("Existing the Program")
            break
        else:
            print("Invalid choice, Please try again")    

if __name__ == "__main__":
    main()