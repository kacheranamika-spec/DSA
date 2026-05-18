#array Rotation
#question: Rotate an array to the right by a given number of steps.
#sample input: [1, 2, 3, 4, 5], steps = 2
#Expected output: [4, 5, 1, 2, 3]
#arr=[1,2,3,4,5] k=2[]-> [4,5,1,2,3]
# enter size
arr = [1, 2, 3, 4, 5]

k = int(input("Enter k: "))

n = len(arr)

for i in range(k):

    temp = arr[n - 1]

    
    for j in range(n - 1, 0, -1):
        arr[j] = arr[j - 1]

    arr[0] = temp

print("Array after rotation:")

for i in range(n):
    print(arr[i], end=" ")