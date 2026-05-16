
# 1       2       3       4
# 5       6       7       8
# 9       10      11      12
# 13      14      15      16

# n=0
# for i in range(1,5):
#     for j in range(1,5):
#         n=n+1
#         print(n,end="\t")
#     print()


# n=64
# for i in range(1,5):
#     for j in range(1,5):
#         n=n+1
#         print(chr(n),end="\t")
#     print()

# for i in range(1,5):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()


# for i in range(4,0,-1):
#     for j in range(1,i+1):
#         print('*',end=" ")
#     print()


# sp=0
# for i in range(4,0,-1):
#     for x in range(sp):
#         print(end=" ")
#     for j in range(1,i+1):
#         print('*',end=" ")
#     print()
#     sp=sp+1

sp=0
for i in range(4,0,-1):
    for x in range(sp):
        print(end=" ")
    for j in range(1,i+1):
        print('*',end=" ")
    print()
    sp=sp+1
