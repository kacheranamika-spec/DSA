# Check for a Valid Palindromic String

# s = input("Enter a string: ")
# new_str = ""
# for ch in s:
#     if ch.isalnum():
#         new_str += ch.lower()
# # Check palindrome using loop
# flag = True
# for i in range(len(new_str) // 2):
#     if new_str[i] != new_str[len(new_str) - 1 - i]:
#         flag = False
#         break
# if flag:
#     print("Valid Palindrome")
# else:
#     print("Not a Palindrome")


# Check for a Valid Palindromic String

s = "A man, a plan, a canal: Panama"
new_str = ""
for ch in s:
    if ch.isalnum():
        new_str += ch.lower()
flag = True
for i in range(len(new_str) // 2):
    if new_str[i] != new_str[len(new_str) - 1 - i]:
        flag = False
        break
if flag:
    print("Valid Palindrome")
else:
    print("Not a Palindrome")