class Node:
    def __init__(self, data=None, next_node=None, prev_node=None):
        '''
        Initialize a node in doubly linked list,
        - data : data to be stored in node
        - next_node : reference to the next node in the list
        - prev_node : reference to the previous node in the list
        '''
        self.data = data
        self.next = next_node
        self.prev = prev_node


class DoublyLinkedList:
    def __init__(self):
        '''
        Initialize a new doubly linked list
        - head : reference to the head (first node) of the doubly linked list
        '''
        self.head = None


    # Insert a node at the beginning of the doubly linked list
    def insert_at_beginning(self, data):
        # Create a new node with the given data, pointing to the current head
        node = Node(data, self.head, None)
        # If the list is not empty, set the previous pointer of the current head to the new node
        if self.head:
            self.head.prev = node
        # Update the head to the new node
        self.head = node


    # Insert a node at the end of the doubly linked list
    def insert_at_end(self, data):
        # If the list is empty, create a new node and set it as the head
        if self.head is None:
            self.head = Node(data, None, None)
            return

        # Iterate to the last node
        itr = self.head
        while itr.next:
            itr = itr.next
        # Create a new node with the given data, pointing to the last node
        itr.next = Node(data, None, itr)


    # Get the length (number of nodes) in the doubly linked list
    def get_length(self):
        count = 0
        itr = self.head
        # Traverse the list and count the nodes
        while itr:
            count += 1
            itr = itr.next
        return count


    # Insert a node at a specified index in the doubly linked list
    def insert_at_index(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception('Invalid Index')

        # If the index is at the beginning, call insert_at_beginning method
        if index == 0:
            self.insert_at_beginning(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                # Create a new node with the given data, adjusting pointers to insert at the specified index
                node = Node(data, itr.next, itr)
                if node.next:
                    node.next.prev = node
                itr.next = node
                break

            itr = itr.next
            count += 1


    # Remove a node at a specified index in the doubly linked list
    def remove_at_index(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception('Invalid Index')

        # If the index is at the beginning, update the head to the next node
        if index == 0:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            return

        count = 0
        itr = self.head
        while itr:
            if count == index:
                # Adjust pointers to remove the node at the specified index
                itr.prev.next = itr.next
                if itr.next:
                    itr.next.prev = itr.prev
                break
            itr = itr.next
            count += 1


    # Insert a node after the first occurrence of a specified value
    def insert_after_value(self, data, data_insert):
        itr = self.head
        while itr:
            if itr.data == data:
                # Create a new node with the given data, adjusting pointers to insert after the specified value
                new_node = Node(data_insert, itr.next, itr)
                if new_node.next:
                    new_node.next.prev = new_node
                itr.next = new_node
                break
            itr = itr.next


    # Remove the first occurrence of a specified value in the doubly linked list
    def remove_by_value(self, data):
        itr = self.head

        while itr:
            if itr.data == data:
                if itr.prev:
                    # Adjust pointers to remove the node with the specified value
                    itr.prev.next = itr.next
                else:
                    # If the node to be removed is the head, update the head to the next node
                    self.head = itr.next

                if itr.next:
                    itr.next.prev = itr.prev

                return
            itr = itr.next

        raise ValueError(f'{data} not found in DoublyLinkedList')


    # Print the doubly linked list in the forward direction
    def print_forward(self):
        if self.head is None:
            print("Doubly Linked List is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + ' <--> '
            itr = itr.next
        print(llstr)


    # Print the doubly linked list in the backward direction
    def print_backward(self):
        if self.head is None:
            print("Doubly Linked List is empty")
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        llstr = ''
        while itr:
            llstr += str(itr.data) + ' <--> '
            itr = itr.prev
        print(llstr)


dll = DoublyLinkedList()

dll.insert_at_beginning(50)
dll.insert_at_beginning(34)
dll.insert_at_beginning(69)
dll.insert_at_beginning(90)

dll.insert_at_end(111)
dll.insert_at_end(321)
dll.insert_at_end(1000)
dll.insert_at_end(2023)

dll.print_forward()
dll.print_backward()

print('Length: ', dll.get_length())

dll.insert_at_index(3, 88)
dll.print_forward()

dll.remove_at_index(7)
dll.print_forward()

dll.insert_after_value(88, 99)
dll.print_forward()

dll.remove_by_value(34)
dll.print_forward()
