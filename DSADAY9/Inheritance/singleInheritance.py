# single inheritance 

class A:
    def showA(self):
        print("i am in class A")
class B:
    def showB(self):
        print("I am in class B")

if __name__ == '__main__':
    obj=B()
    obj.showA()
    obj.showB()               