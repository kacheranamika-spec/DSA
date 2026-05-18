
#delete key element from array
# enter size
size = int(input("Enter size of array: "))
arr = []
# input array elements
for i in range(size):
    element = int(input("Enter element: "))
    arr.append(element)
key = int(input("Enter element to delete: "))
found = False
for i in range(size):
    if arr[i] == key:
        found = True
        for j in range(i, size - 1):
            arr[j] = arr[j + 1]
        break
if found:
    arr.pop()  # decrease array size
    print("Array after deletion:")
    for i in range(size - 1):
        print(arr[i], end=" ")
else:
    print("Element not found in array.")
