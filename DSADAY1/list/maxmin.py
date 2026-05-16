ls = [5, 3, 9, 2, 8]
max_num = ls[0]
for i in range(len(ls)):
    if max_num < ls[i]:
        max_num = ls[i]
print("The maximum number is:", max_num)
min_num = ls[0]
for i in range(len(ls)):
    if min_num > ls[i]:
        min_num = ls[i]
print("The minimum number is:", min_num)