#insert array in the array 
# enter size
size = int(input("Enter size of array: "))

arr = []

# input array elements
for i in range(size):
    element = int(input("Enter element: "))
    arr.append(element)

key = int(input("Enter element to insert: "))
loc = int(input("Enter location: "))


arr.append(0)   # increase array size

for i in range(size, loc, -1):
    arr[i] = arr[i - 1]

arr[loc] = key

print("Array after insertion:")
for i in range(size + 1):
    print(arr[i], end=" ")

    