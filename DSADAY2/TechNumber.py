# num = int(input("Enter number: "))
# temp = num
# digits = len(str(num))
# if digits % 2 == 0:
#     half = digits // 2
#     divisor = 10 ** half
#     first = num // divisor
#     second = num % divisor
#     s = first + second
#     if s * s == temp:
#         print(num, "is a Tech Number")
#     else:
#         print(num, "is not a Tech Number")
# else:
#     print(num, "is not a Tech Number")



# o=int(input("Enter number: "))
# n1=no%100
# n2=no//100
# sum=n1+n2
# sq=sum*sum
# if sq==no:
#     print("Technumber")
# else:
#     print("Not a Technumber")


# Find no is tech no. or not

n = input("Enter a no: ")
num = int(n)
length = len(n)
if length % 2 == 0:
    half = length // 2
    left = int(n[:half])
    right = int(n[half:])
    sum = left + right
    result = (sum) ** 2
    print("Sum =", sum)
    if result == num:
        print(num, "is a Tech num.")
    else:
        print(num, "is not a Tech num.")
else:
    print("Invalid: Tech nums must have an even num of digits.")