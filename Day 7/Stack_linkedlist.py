#Implement Stack using single linkedlist
import sys
class getnode:
    def __init__(self):
        self.data = None
        self.next= None

class Linkedlist_Stack:
    def __init__(self):
        self.head = None
        self.top = None
    
    def push(self):
        data = int(input("Enter data: "))
        newnode = getnode()
        newnode.data=data
        if self.head == None:
            self.head=newnode
        else:
            ptr = self.head
            newnode.next = ptr
            self.head=newnode
            self.top = newnode
            print(data," is added")
            
    def traverse(self):
        if self.head==None:
            print("Linked List not present")
        else:
            ptr = self.head
            while ptr != None:
                print("||",ptr.data,"||")
                ptr=ptr.next

    def peek(self):
        if self.head == None:
            print("Stack is Empty")
        else:
            ele = self.top.data
            print(ele)
    def pop(self):
        if self.head==None:
            print("List is empty")
        else:
            ptr=self.head
            self.head = ptr.next
            print(" Element Popped")


if __name__ == '__main__':
        obj = Linkedlist_Stack()
        while True:
            print("\n1. Append")
            print("2. Pop ")
            print("3. Peek ")
            n = int(input("Enter choice: "))

            if n==1:
                obj.push()
                obj.traverse()
            elif n==2:
                obj.pop()
                print("Remaining Stack: ")
                obj.traverse()
            elif n==3:
                obj.peek()
                
            elif n==0:
                sys.exit(0)
