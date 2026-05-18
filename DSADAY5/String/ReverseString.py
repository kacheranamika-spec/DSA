# Reverse the string 
string = "hello"
reverse = ""

for i in range(len(string) - 1, -1, -1):
    reverse = reverse + string[i]

print("Reversed string is:")
print(reverse)