from collections import deque

class Queue:
    def __init__(self):
        self.container = deque()

    def enqueue(self, val):
        self.container.appendleft(val)

    def deque(self):
        if len(self.container) == 0:
            print('Queue is empty')
        return self.container.pop()
    
    def pop(self):
        return self.container.pop()
    
    def size(self):
        return len(self.container)
    
    def display(self):
        return self.container
    
queue = Queue()

orders = ['butter_chicken', 'tandoori_chicken', 'chicken_roasted', 'chicken_grilled', 'heroine']

for food in orders:
    queue.enqueue(food)
    print('orders : ', queue.display())

print('\n queue : ', queue.display())

queue.deque()
print()
print(queue.display())
