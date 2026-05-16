# arr = []

# n = int(input("Enter size: "))

# print("Enter list elements:")

# for i in range(n):
#     ele = int(input("Enter element: "))
#     arr.append(ele)

# even_sum = 0
# odd_sum = 0

# for i in arr:
#     if i % 2 == 0:
#         even_sum += i
#     else:
#         odd_sum += i

# print("Sum of even numbers:", even_sum)
# print("Sum of odd numbers:", odd_sum)



arr = []
n = int(input("Enter size: "))
print("Enter list elements:")
for i in range(n):
    ele = int(input("Enter element: "))
    arr.append(ele)
even_sum = 0
odd_sum = 0
even_count = 0
odd_count = 0
for i in arr:
    if i % 2 == 0:
        even_sum += i
        even_count += 1
    else:
        odd_sum += i
        odd_count += 1
print("Sum of even numbers:", even_sum)
print("Total even numbers:", even_count)
print("Sum of odd numbers:", odd_sum)
print("Total odd numbers:", odd_count)