# def add():
#     a = int(input("Enter a: "))
#     b = int(input("Enter b: "))
#     res = a+b
#     print("Addition is ",res)

# if __name__ == "__main__":
#     add()

#function with parameters
# def add(a,b):
#     res = a+b
#     print("Addition is ",res)
# if __name__ == "__main__":
#      a = int(input("Enter a: "))
#      b = int(input("Enter b: "))
#      add(a,b)

#function with parameters and return type
# def add(a,b):
#     res = a+b
#     return res
    
# if __name__ == "__main__":
#      a = int(input("Enter a: "))
#      b = int(input("Enter b: "))
#      add(a,b)  
#      print("Addition is ",res)



# function with parameters and return multiple values
def add(a, b):
    res1 = a + b
    res2 = a - b
    res3 = a * b
    return res1, res2, res3
if __name__ == "__main__":
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    r1, r2, r3 = add(a, b)
    print("Addition is", r1)
    print("Subtraction is", r2)
    print("Multiplication is", r3)

