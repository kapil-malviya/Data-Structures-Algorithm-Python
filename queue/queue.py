from collections import deque

class Queue:

    def __init__(self):
        self.container = deque()

    def enqueue(self, val):
        self.container.appendleft()

    def deque(self):
        if len(self.container) == 0:
            print('Empty')
        return self.container.pop()
    
    def pop(self):
        return self.container.pop()
    
    def size(self):
        return len(self.container)

    def display(self):
        return self.container
    

my_queue = Queue()

# Enqueue some values
my_queue.enqueue(10)
my_queue.enqueue(20)
my_queue.enqueue(30)

# display the size of the queue
print('Size of the queue : ', my_queue.size())

# dequeue and display the removed element
removed_element = my_queue.dequeue()
print('Removed element : ', removed_element)

# display the size of the queue after dequeuing
print('Size of the queue after dequeue : ', my_queue.size())

# pop an element from the end of the queue
popped_element = my_queue.pop()
print('Popped element : ', popped_element)

# size of queue after popping
print('Size of the queue after pop : ', my_queue.size())
