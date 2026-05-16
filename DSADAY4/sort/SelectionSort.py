# SelectionSort
# def selectionSort(arr):
#     for i in range(len(arr)):
#         min_index = i
#         for j in range(i + 1, len(arr)):
#             if arr[j] < arr[min_index]:
#                 min_index = j
#         arr[i], arr[min_index] = arr[min_index], arr[i]

# if __name__ == "__main__":
#     arr = [6, 23, 2, 4, 1, 8, 56, 3]
#     selectionSort(arr)
#     print(*arr) 


    # Descending order 
def selectionSort(arr):
    for i in range(len(arr)):
        max_index = i                        
        for j in range(i + 1, len(arr)):
            if arr[j] > arr[max_index]:     
                max_index = j
        arr[i], arr[max_index] = arr[max_index], arr[i]  

if __name__ == "__main__":
    arr = [6, 23, 2, 4, 1, 8, 56, 3]
    selectionSort(arr)
    print(*arr)

    