#reverse array using stack
# arr=[23,45,12,67,34]
# reverse array using stack

class Stack:
    def __init__(self):
        self.stack = []
    def push(self, ele):
        self.stack.append(ele)
    def pop(self):
        return self.stack.pop()
    def isEmpty(self):
        return len(self.stack) == 0
    
def reverseArray(arr):
    s = Stack()
    print("Pushing elements into stack:")
    for ele in arr:
        s.push(ele)
        print(ele, "pushed →  Stack:", s.stack)
    print("\nPopping elements from stack:")
    for i in range(len(arr)):
        arr[i] = s.pop()
        print(arr[i], "popped →  Array:", arr[:i+1])
    return arr

arr = [23, 45, 12, 67, 34]
print("Original Array:", arr)
print()
reverseArray(arr)
print("\nReversed Array:", *arr)


