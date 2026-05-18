# import sys
# class Queue:
#     def __init__(self):
#         self.queue=[]
#         self.rear=-1
#         self.front=0
#         self.CAPACITY=5

#     def isFull(self):
#         if self.rear==self.CAPACITY-1:
#             return True
#         else:
#             return False

#     def insert(self,ele):
#         if self.isFull():
#             print("queue is full")
#         else:
#             self.rear=self.rear+1
#             self.queue.append(ele)
#             print(ele, "is inserted")

#     def traverse(self):
#         if self.isEmpty():
#             print("Queue is empty")

#         else:
#             print("Queue elements are:")

#             for i in range(self.front, self.rear + 1):
#                 print(self.queue[i])


#     def isEmpty(self):
#         if self.rear==-1:
#             return True
#         else:
#             return False

#     def delete(self):
#         pass
        
    
#     def peek(self):
#          if self.isEmpty():
#             print("Queue is empty")
#          else:
#              print("Queue elements are")   

# if __name__ == '__main__':
#     obj=Queue()
#     while True:
#         print("1. insert")
#         print("2. delete")
#         print("3. Peek")
#         print("4. Traverse")
#         print("0. Exit")
#         ch=int(input("select any choice"))
#         if ch==1:
#             ele=int(input("Enter data: "))
#             obj.insert(ele)
#         elif ch==2:
#             obj.delete()
#         elif ch==3:
#             obj.peek()
#         elif ch==4:
#             obj.traverse()
#         elif ch==0:
#             sys.exit(0)



import sys
class Queue:
    def __init__(self):
        self.queue = []
        self.front = -1
        self.rear = -1
        self.CAPACITY = 5
    def isFull(self):
        return self.rear == self.CAPACITY - 1
    def isEmpty(self):
        return self.front == -1 or self.front > self.rear
    def enqueue(self, ele):
        if self.isFull():
            print("Queue is full")
        else:
            if self.front == -1:
                self.front = 0
            self.rear += 1
            self.queue.append(ele)
            print(ele, "is inserted")
    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            ele = self.queue[self.front]
            self.front += 1
            print(ele, "is deleted")
    def peek(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            print("Front element is:", self.queue[self.front])
    def traverse(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            print("Queue elements are:")
            for i in range(self.front, self.rear + 1):
                print(self.queue[i])
if __name__ == '__main__':
    obj = Queue()
    while True:
        print("\n1.Enqueue")
        print("2.Dequeue")
        print("3.Peek")
        print("4.Traverse")
        print("0.Exit")
        ch = int(input("Select any choice: "))
        if ch == 1:
            ele = int(input("Enter element: "))
            obj.enqueue(ele)
        elif ch == 2:
            obj.dequeue()
        elif ch == 3:
            obj.peek()
        elif ch == 4:
            obj.traverse()
        elif ch == 0:
            sys.exit(0)
        else:
            print("Invalid choice")