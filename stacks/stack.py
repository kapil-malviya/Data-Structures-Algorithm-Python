from collections import deque

class Stack:
    def __init__(self):
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

stack = Stack()

stack.push(8)
stack.push(808)
stack.push(8008)

print('\nstack :', stack.display())
print('size : ', stack.size())
print('peek : ', stack.peek())  
print('pop : ', stack.pop())    
print('size : ', stack.size())   
print()