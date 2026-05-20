s = "ycce"
t = "ycsce"

# mid = len(s)//2
# st1 = s[:mid]
# st2 = s[mid:]

# st1 +=  "s" + st2
# count = 0
# for i in range(len(s)):
#     if s[i]==t[i]:
#         print(0)
#     else:
#         count += 1
# print(st1)

output = 0
count = 0
if len(s)<len(t):
    output=len(t)-len(s)
elif len(t)<len(s):
    output = len(s)-len(t)
elif len(s)==len(t):
    for i in range(len(s)):
        if s[i]!=t[i]:
            count = count+1
    output = count
    print(output)