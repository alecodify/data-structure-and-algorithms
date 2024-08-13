"""
A priority queue is a special type of queue in which each element is associated with a priority value. And, elements are served on the basis of their priority. 
That is, higher priority elements are served first.
However, if elements with the same priority occur, they are served according to their order in the queue.
"""

def heapify(arr, n, i):
    # Heapify a subtree rooted with node i, which is an index in arr[]. n is the size of the loop.
    largest = i    # Initialize largest as root.
    l = 2 * i + 1  # Left child index = 2*i + 1
    r = 2 * i + 2  # Right child index = 2*i + 2

    # If the left child exists and is greater than root, update largest.
    if l < n and arr[i] < arr[l]:
        largest = l

    # If the right child exists and is greater than the largest so far, update largest.
    if r < n and arr[largest] < arr[r]:
        largest = r

     # If the largest is not root, swap it with the largest and continue heapifying.
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def insert(array, newNum):
    size = len(array)
    if size == 0:
        array.append(newNum)
    else:
        array.append(newNum)
        # Heapify the tree starting from the last non-leaf node to the root.
        for i in range((size // 2) - 1, -1, -1):
            heapify(array, size, i)


def deleteNode(array, num):
    size = len(array)
    i = 0
    # Find the index of the element to be deleted.
    for i in range(0, size):
        if num == array[i]:
            break
    
    # Swap the element to be deleted with the last element.
    array[i], array[size - 1] = array[size - 1], array[i]

    # Remove the last element
    array.remove(size - 1)

    # Heapify the root node to maintain the max-heap property.
    for i in range((len(array) // 2) - 1, -1, -1):
        heapify(array, len(array), i)


arr = []

insert(arr, 3) # After this operation, the array is [3]
insert(arr, 4) # After this operation, the array becomes [4, 3]. Heapify ensures the max-heap property, so 4 is placed at the root
insert(arr, 9) # After this operation, the array becomes [9, 3, 4]. 9 is larger than the root (4) then it swap 
insert(arr, 5) # After this operation, the array becomes [9, 5, 4, 3]
insert(arr, 2) # After this operation, the array becomes [9, 5, 4, 3, 2]

print ("Max-Heap array: " + str(arr))

deleteNode(arr, 4)
print("After deleting an element: " + str(arr))