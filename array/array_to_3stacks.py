from collections import deque

class Stack:
    def _init_(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def peek(self):
        return self.container[-1]
    
    def pop(self):
        return self.container.pop()
    
    def size(self):
        return len(self.container)
    
    def display(self):
        return self.container
    
stack1 = Stack()
stack2 = Stack()
stack3 = Stack()


array = [ num for num in range(1, 101)  ]

for num in range(len(array)):
    
    if num < 33:
        stack1.push(array[num])

    if num >33 and num < 66 :
        stack2.push(array[num])

    if num > 66:
        stack3.push(array[num])


print(stack1.display())
print(stack2.display())
print(stack3.display())