def multiply(a,b):
    if b==1:
        return a
    elif a==1:
        return b
    elif a==0 or b==0:
        return 0
    else:
        return a+multiply(a,b-1)

print(multiply(5,3))