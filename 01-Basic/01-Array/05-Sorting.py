def main():
    length = int(input("Enter the length of the array: "))
    array = []

    for i in range(length):
        element = int(input(f"Enter element {i + 1}: "))
        array.append(element)
    
    print("Original Array: ", array)
    
    array.sort()
    print("Sort Array", array)

if __name__ == "__main__":
    main()