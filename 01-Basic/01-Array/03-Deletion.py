def deleteFromBegining(array):
    if len(array) == 0:
        print("Array is empty. Cannot Delete.")
        return array
    deletedElement = array.pop(0)
    print(f"Deleted element from begining: {deletedElement}")
    return array

def deleteFromEnd(array):
    if len(array) == 0:
        print("Array is empty. Cannot Delete.")
        return array
    deleteElement = array.pop()
    print(f"Deleted element from end: {deleteElement}")
    return array

def deleteFromIndex(array, index):
    if index < 0 or index >= len(array):
        print("Index out of bounds")
        return array
    deleteElement = array.pop(index)
    print(f"Deleted element from index {index}: {deleteElement}")
    return array

def main():
    length = int(input("Enter the length of the array: "))
    array = []

    for i in range(length):
        element = input(f"Enter element {i + 1}: ")
        array.append(element)

    print("Initial Array: ", array)

    while True:
        print("\nChoose a deletion option:")
        print("1. Delete from the begining")
        print("2. Delete from the end")
        print("3. Delete from a specific index")
        print("4. Exit")
        
        choice = int(input("Enter your choice: "))

        if choice == 1:
            deleteFromBegining(array)
            print(array)
        
        elif choice == 2:
            deleteFromEnd(array)
            print(array)
        
        elif choice == 3:
            index = int(input("Enter the index to delete from: "))
            deleteFromIndex(array, index)
            print(array)

        elif choice == 4:
            print("Existing the program.")
            break

        else:
            print("Invalid choice. Please try again.")
        
if __name__ == "__main__":
    main()
