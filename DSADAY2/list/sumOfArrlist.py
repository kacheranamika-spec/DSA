# arr = []
# n = int(input("Enter size: "))
# print("Enter list elements:")
# for i in range(n):
#     ele = int(input("Enter element: "))
#     arr.append(ele)
# total = sum(arr)
# print("Sum of list:", total)


# arr = []
# n = int(input("Enter size: "))
# print("Enter list elements:")
# for i in range(n):
#     ele = int(input("Enter element: "))
#     arr.append(ele)
# total = 0
# for i in arr:
#     total += i
# print("Sum of list:", total)


n=int(input("Enter size: "))
print("Enter list elements:")       
arr=[]
sum=0
for i in range(n):
    ele=int(input("Enter element: "))
    arr.append(ele)
    for i in range(len(arr)):
        sum+=arr[i]