CAPACITY = 5
class Queue:
    def __init__(self):
        self.queue=[]
        self.rear=-1
        self.front=0
        self.CAPACITY=5

    def isFull(self):
        if self.rear==self.CAPACITY-1:
            return True
        else:
            return False

    def insert(self,ele):
        if self.isFull():
            print("queue is full")
        else:
            self.rear=self.rear+1
            self.queue.append(ele)
            print(ele, "is inserted")

    def traverse(self):
        if self.isEmpty():
            print("Queue is empty")

        else:
            print("Queue elements are:")

            for i in range(self.front, self.rear + 1):
                print(self.queue[i])


    def isEmpty(self):
        if self.rear==-1:
            return True
        else:
            return False

    def delete(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            ele=self.queue[self.front]
            for i in range(1, self.front+1):
                Queue[i-1]= Queue[i]
            self.rear-1 
        return ele       
    
    def peekFront(self):

        if self.isEmpty():
            print("Queue is empty")

        else:
            print("Front element is:", self.queue[self.front])

    def peekRear(self):

        if self.isEmpty():
            print("Queue is empty")

        else:
            print("Rear element is:", self.queue[self.rear])
            
class Stack:

    def __init__(self):
        self.stack = []
        self.top = -1
        self.CAPACITY = 5

    def isFull(self):
        if self.top == self.CAPACITY - 1:
            return True
        else:
            return False

    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False
        

    def push(self, ele):
        if self.isFull():
            print("Stack is full")
        else:
            self.top = self.top + 1
            self.stack.append(ele)
            print(ele, "is pushed")

    def pop(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            ele = self.stack.pop()
            self.top = self.top - 1
            print(ele, "is popped")

    def peek(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            print("Top element is:", self.stack[self.top])

    def traverse(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            print("Stack elements are:")
            for i in range(self.top, -1, -1):
                print(self.stack[i])
                
if __name__ == '__main__':
    obj1= Queue()
    obj2= Stack()
    for i in range(obj1.CAPACITY):
        ele=int(input("enter element"))
        obj1.insert(ele)
        
    for i in range(obj1.CAPACITY):
        ele=obj1.delete()
        obj2.push(ele)
        
    for i in range(obj1.CAPACITY) :
        ele = obj2.pop()
        obj1.insert(ele)
        
    print("\nReversed Queue:")
    obj1.traverse()