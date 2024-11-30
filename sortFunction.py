def sort(a):
    return sorted(a)

def insertionsort(b):
    n = len(b)  # Get the length of the array

    if n <= 1:
        return b # If the array has 0 or 1 element, it is already sorted, so return

    for i in range(1, n):  # Iterate over the array starting from the second element
        print("aktuelles Array: ", b)
        key = b[i]  # Store the current element as the key to be inserted in the right position
        print("aktuelle Zahl: ", key)
        j = i - 1
        while j >= 0 and key < b[j]:  # Move elements greater than key one position ahead
            print("Vergleichswert: ", b[j])
            b[j + 1] = b[j]  # Shift elements to the right
            j -= 1
            print("verschobene Werte: ", b)
        b[j + 1] = key  # Insert the key in the correct position
        print("Array mit eingefügten Werten: ", b)
    return b