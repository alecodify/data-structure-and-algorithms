def LinearSearch(array, target):
    for index, element in enumerate(array):
        if element == target:
            return index
    
    return -1;

def BinarySearch(array, target):
    left, right = 0, len(array) - 1;

    while left <= right:
        mid = left + (right - left) // 2

        if array[mid] == target:
            return mid
        
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

def main():
    length = int(input("Enter the length of the array: "))
    array = []

    for i in range(length):
        element = int(input(f"Enter element {i + 1}: "))
        array.append(element)

    print("Array: ",  array)

    targetElement = int(input("Enter the element to search for: "))
    
    while True:
        print("\nChoose the search method:")
        print("1. Linear Search")
        print("2. Binary Search (Array must be sorted)")
        print("3. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            result = LinearSearch(array, targetElement)
        elif choice == 2:
            array.sort()
            print(f"Sorted Array: ", array)
            result = BinarySearch(array, targetElement)
    
        elif choice == 3:
            print("Existing the program.")
            break;

        else:
            print("Invalid choice. Please try again.")

        if result != -1:
            print(f"Element {targetElement} found at index: {result}")
        else:
            print(f"Element {targetElement} not found in the array")

if __name__ == "__main__":
    main()