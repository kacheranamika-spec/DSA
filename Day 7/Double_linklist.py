import sys
class getnode:
    def __init__(self):
        self.right = None
        self.data = None
        self.right = None
    
class Linkedlist:
    def __init__(self):
        self.head = None
    

    def append(self):
        data = int(input("Enter data:"))
        newnode = getnode()
        newnode.data = data
        if self.head is None:
            self.head = newnode
        else:
            ptr = self.head
            while ptr.right != None:
                ptr = ptr.right
            ptr.right =newnode
            newnode.left = ptr
            print(data," is added")

    def traverse(self):
        if self.head is None:
            print("List not present")
        else:
            ptr = self.head
            while ptr != None:
                print(ptr.data," -> ",end="")
                ptr = ptr.right
    
    def addbegin(self):
        newnode = getnode()
        data = int(input("Enter value: "))
        newnode.data = data
        if self.head is None:
             self.head=newnode
        else:
            ptr = self.head
            self.head = newnode
            ptr.left = newnode
            newnode.right = ptr

    def addbetween(self):
        newnode = getnode()
        key = int(input("Enter Key value: "))
        data = int(input("Enter value:"))
        newnode.data = data

        if self.head is None:
            self.head=newnode
        else:
            ptr = self.head
            while ptr.right != None:
                if key==ptr.data:
                    break
                else:
                    ptr = ptr.right
            if key!= ptr.data:
                print("Key not present")
            else:
                ptr1 = ptr.right
                ptr.right = newnode
                newnode.right = ptr1
                newnode.left = ptr
                print("new node added")

    def deletebegin(self):
        if self.head is None:
         print("List not exist")
        else:
            ptr = self.head
            ptr1 = ptr.right
            # ptr1.left = None
            self.head = ptr1
            print("Begin Node deleted")


if __name__ == '__main__':
    obj = Linkedlist()
    while True:
        print("\n1. Append")
        print("2. Traverse ")
        print("3. Add at Beginning")
        print("4. Add in between ")
        print("5. Delete at Beginning")
        print("6. Delete at End")
        print("7. Delete any node")
        print("0. Exit")
        n = int(input("Enter choice: "))

        if n==1:
            obj.append()
            obj.traverse()
        elif n==2:
            obj.traverse()
        elif n==3:
            obj.addbegin()
            obj.traverse()
        elif n==4:
            obj.addbetween()
            obj.traverse()
        elif n==5:
            obj.deletebegin()
            obj.traverse()
        elif n==0:
            sys.exit(0)

        
