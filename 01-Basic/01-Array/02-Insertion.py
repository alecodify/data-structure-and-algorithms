def insertAtBegining(array, element):
    array.insert(0, element)

def insertAtEnd(array, element):
    array.append(element)

def insertAtIndex(array, element, index):
    if index < 0 or index > len(array):
        print("Index out of bounds")
        return
    array.insert(index, element)

def main():
    length = int(input("Enter the length of array: "))
    array = []

    for i in range(length):
        element = input(f"Enter element {i + 1}: ")
        array.append(element)
    
    print("Initial Array: ", array)

    while True:
        print("\nChoose an insertion option: ")
        print("1. Insert at the begining")
        print("2. Insert at the end")
        print("3. Insert at the specific index")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            element = input("Enter the element to insert at beginging: ")
            insertAtBegining(array, element)
            print(array)

        elif choice == 2:
            element = input("Enter the element to insert at the end: ")
            insertAtEnd(array, element)
            print(array)
        
        elif choice == 3:
            element = input("Enter the element to insert: ")
            index = int(input("Enter the index to insert at: "))
            insertAtIndex(array, element, index)
            print(array)

        elif choice == 4:
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again")

if __name__ == "__main__":
    main()