# find mix and max 

import sys
class getnode:
    def __init__(self):
        self.data = None
        self.front = None
        self.rear= None

class Queue:
    def __init__(self):
        self.head=None
    
    def append(self):
        data = int(input("Enter data: "))
        newnode = getnode()
        newnode.data=data
        if self.head == None:
            self.head=newnode
        else:
            ptr = self.head
            while ptr.rear != None:
                ptr = ptr.rear
            ptr.rear=newnode
            print(data," is added to queue")

    def traverse(self):
        if self.head==None:
            print("Linked List not present")

        else:
            print("Front: ",end =" ")
            ptr = self.head
            while ptr != None:
                print(ptr.data," <- ", end=" ")
                ptr=ptr.rear
    
    def delete_begin(self):
        if self.head==None:
            print("List is empty")
        else:
            ptr=self.head
            self.head = ptr.rear
            print("Begin node is deleted")
    
if __name__ == "__main__":
    obj = Queue()
    
    while True: 
        print("\n1. Append")
        print("2. Traverse")
        print("3. Delete ")
        print("0. Exit")
        n = int(input("Select any Object: "))

        if n ==1:
            obj.append()
            obj.traverse()
        elif n==2:
            obj.traverse()
        elif n==3:
            obj.delete_begin()
            obj.traverse()

        elif n==0:
            sys.exit()
