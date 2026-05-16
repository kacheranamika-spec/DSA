#ascending order
# arr = [5,2,17,3,4,9,15,1]
# for i in range(1, len(arr)):
#     current = arr[i]
#     pos = i 
#     while current<arr[pos-1] and pos>0:
#         arr[pos] = arr[pos-1]
#         pos=pos-1
#     arr[pos] = current
# print(*arr)


#descending order
arr = [5, 2, 17, 3, 4, 9, 15, 1]
for i in range(1, len(arr)):
    current = arr[i]
    pos = i
    while pos > 0 and current > arr[pos - 1]:  
        arr[pos] = arr[pos - 1]
        pos = pos - 1
    arr[pos] = current                          
print(*arr)