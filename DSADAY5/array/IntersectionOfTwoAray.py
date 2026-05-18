

# intersection of array 
arr1 = [1, 2, 2, 1]
arr2 = [2, 2]
arr3 = []

for i in range(len(arr1)):

    for j in range(len(arr2)):

        if arr1[i] == arr2[j]:

            # Store only once
            if arr1[i] not in arr3:
                arr3.append(arr1[i])

            break

print("Intersection array is:")

for i in range(len(arr3)):
    print(arr3[i], end=" ")