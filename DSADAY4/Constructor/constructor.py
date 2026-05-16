# class Student:
#     def __init__(self):
#         print("default constructor")

#         def __init__(self, name):
#             print("I am in show")
# s = Student();
# s.show();



class Student:
    def __init__(self):
        print("default constructor")
    def __init__(self, a): 
        print(a)
    def __init__(self, a,b):
        print(a,b)
    def show(self):
        print("I am in show")

s = Student(10,20)
s.show()
           

        