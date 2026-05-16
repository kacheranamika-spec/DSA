# d={}
# d[100]="ashish"
# d[200]="sachin"
# d[300]="rohit"
# print(d)

rec={}
n=int(input("Enter number of students: "))
for i in range(n):
    name=input("Enter name: ")
    per = float(input("Enter percentage: "))
    rec[name]=per
print(rec)
for x in rec:
    print(x,rec[x])



#     d={}
# d[100]="chetna"
# d[200]="shrishti"
# d[300]="anamika"
# print(d)

