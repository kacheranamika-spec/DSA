# arr = [[1,2,3],[4,5,6],[7,8,9]]
# print(arr)
# for i in range(len(arr)):
#     for j in range(len(arr[i])):
#         print(arr[i][j])

arr = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
print(arr)
for x in range(len(arr)):
    print(arr[x])

    for i in range(len(arr)):
        
        for j in range(len(arr[i])):
             print(arr[i][j],end=" ")
        print()