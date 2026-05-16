
# import sys

# class Stack:                                     
#     def __init__(self):
#         self.stack = []
#     def push(self):
#         element = int(input("Enter element to push: "))
#         self.stack.append(element)
#         print(f"{element} pushed to stack")
#         print("Stack:", self.stack)
#     def pop(self):
#         if len(self.stack) == 0:
#             print("Stack is empty!")
#         else:
#             removed = self.stack.pop()
#             print(f"{removed} popped from stack")
#             print("Stack:", self.stack)
#     def traverse(self):
#         if len(self.stack) == 0:
#             print("Stack is empty!")
#         else:
#             print("Stack elements (top to bottom):")
#             for i in range(len(self.stack) - 1, -1, -1):
#                 print(self.stack[i])
#     def peek(self):
#         if len(self.stack) == 0:
#             print("Stack is empty!")
#         else:
#             print(f"Top element: {self.stack[-1]}")
# if __name__ == "__main__":
#     obj = Stack()                               
#     while True:
#         print("\n1. Push")
#         print("2. Pop")
#         print("3. Traverse")
#         print("4. Peek")
#         print("5. Exit")
#         choice = int(input("Select your choice: "))
#         if choice == 1:
#             obj.push()
#         elif choice == 2:
#             obj.pop()
#         elif choice == 3:
#             obj.traverse()
#         elif choice == 4:
#             obj.peek()
#         elif choice == 5:
#             sys.exit(0)




# import sys
# class Stack:
#     def __init__(self):
#         self.stack = []
#         self.top = -1
#         self.CAPACITY = 5
#     def isFull(self):
#         return self.top == self.CAPACITY - 1
#     def isEmpty(self):
#         return self.top == -1
#     def push(self, ele):
#         if self.isFull():
#             print("Stack is Full!")
#         else:
#             self.top += 1
#             self.stack.append(ele)
#             print(ele, "is pushed")
#             print("Stack:", self.stack)
#     def pop(self):
#         if self.isEmpty():
#             print("Stack is Empty!")
#         else:
#             ele = self.stack.pop()
#             self.top -= 1
#             print(ele, "is popped")
#             print("Stack:", self.stack)
#     def peek(self):
#         if self.isEmpty():
#             print("Stack is Empty!")
#         else:
#             print("Top element is:", self.stack[self.top])
#     def traverse(self):
#         if self.isEmpty():
#             print("Stack is Empty!")
#         else:
#             print("Stack elements (top to bottom):")
#             for i in range(self.top, -1, -1):
#                 print(self.stack[i])
# obj = Stack()
# while True:
#     print("\n1. Push")
#     print("2. Pop")
#     print("3. Peek")
#     print("4. Traverse")
#     print("0. Exit")
#     ch = int(input("Select any choice: "))
#     if ch == 1:
#         ele = int(input("Enter data: "))
#         obj.push(ele)
#     elif ch == 2:
#         obj.pop()
#     elif ch == 3:
#         obj.peek()
#     elif ch == 4:
#         obj.traverse()
#     elif ch == 0:
#         print("Exiting...")
#         sys.exit()
#     else:
#         print("Invalid choice")





# import sys
# class Stacks:
#     def __init__(self):
#         self.stack = []
#         self.top = -1
#         self.CAPACITY = 5

#     def isFull(self):
#         if self.top == self.CAPACITY - 1:
#             return True
#         else:
#             return False

#     def isEmpty(self):
#         if self.top == -1:
#             return True
#         else:
#             return False

#     def push(self, ele):
#         if self.isFull():
#             print("Stack is full")
#         else:
#             self.top = self.top + 1
#             self.stack.append(ele)
#             print(ele, "is pushed")

#     def pop(self):
#         if self.isEmpty():
#             print("Stack is empty")
#         else:
#             ele = self.stack[self.top]
#             self.stack.pop()
#             self.top = self.top - 1
#             return ele

#     def peek(self):
#         if self.isEmpty():
#             print("Stack is empty")
#         else:
#             print("Top element is:", self.stack[self.top])

#     def traverse(self):
#         if self.isEmpty():
#             print("Stack is empty")
#         else:
#             print("Stack elements are:")
#             for i in range(self.top, -1, -1):
#                 print(self.stack[i])

# if __name__ == '__main__':

#     obj = Stacks()
#     while True:
#         print("\n1. Push")
#         print("2. Pop")
#         print("3. Peek")
#         print("4. Traverse")
#         print("0. Exit")
#         ch = int(input("Select any choice: "))
#         if ch == 1:
#             ele = int(input("Enter data: "))
#             obj.push(ele)
#         elif ch == 2:
#             ele = obj.pop()
#             if ele is not None:
#                 print(ele, "is popped")
#         elif ch == 3:
#             obj.peek()
#         elif ch == 4:
#             obj.traverse()
#         elif ch == 0:
#             sys.exit()
#         else:
#             print("Invalid choice")







# Stack with capacity 

# import sys
# class Stacks: 
#     def __init__(self, size):
#         self.stack = []
#         self.top = -1
#         self.capacity = size 
#     def isFull(self):
#       if self.top == self.capacity - 1:
#         return True
#       else:
#         return False
#     def push(self, ele):
#       if self.isFull():
#         print("Stack is full")
#       else:
#         self.top += 1
#         self.stack.append(ele)
#         print(f"Pushed {ele} to stack. Current stack: {self.stack}")
#     def isEmpty(self):
#         return self.top == -1
#     def pop(self):
#         if self.isEmpty():
#             print("Stack is empty, cannot pop.")
#             return None
#         else:
#             pop_ele = self.stack.pop()
#             self.top -= 1
#             print(f"Popped {pop_ele}. Current stack: {self.stack}")
#             return pop_ele
#     def peek(self):
#         if self.isEmpty():
#             print("Stack is empty, no element to peek.")
#             return None
#         else:
#             print(f"Top element: {self.stack[self.top]}")
#             return self.stack[self.top]
#     def traverse(self):
#       if self.isEmpty():
#         print("Stack is empty.")
#         return
#       print("Stack elements (top to bottom):")
#       for i in range(self.top, -1, -1):
#         print(self.stack[i])
# if __name__ == '__main__':
#     stack_capacity = int(input("Enter stack capacity: "))
#     obj = Stacks(stack_capacity)
#     while True:
#         print("\n--- Stack Operations ---")
#         print("1. Push")
#         print("2. Pop")
#         print("3. Peek")
#         print("4. Traverse")
#         print("0. Exit")
#         print(f"Current stack size: {obj.top + 1}/{obj.capacity}")
#         try:
#             ch = int(input("select any choice: "))
#         except ValueError:
#             print("Invalid input. Please enter a number.")
#             continue
#         if ch == 1:
#             try:
#                 element = int(input("Enter element to push: "))
#                 obj.push(element)
#             except ValueError:
#                 print("Invalid input. Please enter a number.")
#         elif ch == 2:
#             obj.pop()
#         elif ch == 3:
#             obj.peek()
#         elif ch == 4:
#             obj.traverse()
#         elif ch == 0:
#             sys.exit()
#         else:
#             print("Invalid Choice")









# without capacity
# Stack with capacity 

import sys
class Stacks: 
    def __init__(self, size):
        self.stack = []
        self.top = -1
        self.capacity = size 
    def isFull(self):
      if self.top == self.capacity - 1:
        return True
      else:
        return False
    def push(self, ele):
      if self.isFull():
        print("Stack is full")
      else:
        self.top += 1
        self.stack.append(ele)
        print(f"Pushed {ele} to stack. Current stack: {self.stack}")
    def isEmpty(self):
        return self.top == -1
    def pop(self):
        if self.isEmpty():
            print("Stack is empty, cannot pop.")
            return None
        else:
            pop_ele = self.stack.pop()
            self.top -= 1
            print(f"Popped {pop_ele}. Current stack: {self.stack}")
            return pop_ele
    def peek(self):
        if self.isEmpty():
            print("Stack is empty, no element to peek.")
            return None
        else:
            print(f"Top element: {self.stack[self.top]}")
            return self.stack[self.top]
    def traverse(self):
      if self.isEmpty():
        print("Stack is empty.")
        return
      print("Stack elements (top to bottom):")
      for i in range(self.top, -1, -1):
        print(self.stack[i])
if __name__ == '__main__':
    stack_capacity = int(input("Enter stack capacity: "))
    obj = Stacks(stack_capacity)
    while True:
        print("\n--- Stack Operations ---")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Traverse")
        print("0. Exit")
        print(f"Current stack size: {obj.top + 1}/{obj.capacity}")
        try:
            ch = int(input("select any choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        if ch == 1:
            try:
                element = int(input("Enter element to push: "))
                obj.push(element)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif ch == 2:
            obj.pop()
        elif ch == 3:
            obj.peek()
        elif ch == 4:
            obj.traverse()
        elif ch == 0:
            sys.exit()
        else:
            print("Invalid Choice")





  
