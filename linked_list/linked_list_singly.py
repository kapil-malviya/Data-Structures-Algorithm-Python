import pdb

class Node:
	def __init__(self, data=None, next=None):
		self.data = data
		self.next = next

class LinkedList:
	def __init__(self):
		self.head = None

	def insert_at_begining(self, data):
		node = Node(data, self.head)
		self.head = node

	def display(self):
		if self.head is None:
			print('Linked List is empty')
			return

		itr = self.head
		llstr = ''

		while itr:
			llstr += str(itr.data) + '-->'
			itr = itr.next
			# pdb.set_trace()

		print(llstr)

	def insert_at_end(self, data):
		if self.head is None:
			self.head = Node(data, None)
			return

		itr = self.head

		while itr.next:
			itr = itr.next
		itr.next = Node(data, None)

	def get_length(self):
		count = 0
		itr = self.head
		while itr:
			count += 1
			itr = itr.next
		return count

	def insert_at(self, index, data):
		if index < 0 or index > self.get_length():
			raise Exception('Not a Valid Index')
		
		count = 0
		itr = self.head

		while itr:
			if count == index-1 :
				node = Node(data, itr.next)
				itr.next = node
				break
			itr = itr.next
			count += 1

	def remove_at(self, index):
		if index < 0 or index > self.get_length():
			raise Exception('Not a Valid Index')
		
		if index == 0:
			self.head = self.head.next

		count = 0
		itr = self.head

		while itr:
			if count == index-1 :
				itr.next = itr.next.next
				break

			itr = itr.next
			count += 1

	def insert_after_value(self, data, data_insert):
		if self.head is None:
			raise Exception("List is empty")

		itr = self.head
		while itr:
			if itr.data == data:
				node = Node(data_insert, itr.next)
				itr.next = node
				break
			itr = itr.next


	def remove_by_value(self, data):
		if self.head is None:
			raise Exception("List is empty")

		if self.head.data == data:
			self.head = self.head.next
			return

		itr = self.head
		while itr.next:
			if itr.next.data == data:
				itr.next = itr.next.next
				break
			itr = itr.next



if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_begining(5)
    ll.insert_at_begining(15)
    ll.insert_at_begining(25)
    ll.display()
    x = ll.get_length()
    print('length : ', x)
    ll.insert_at_end(88)
    ll.insert_at_end(8888)
    ll.display()
    print('length : ', ll.get_length())
    ll.insert_at(3, 50)
    ll.display()
    print('length : ', ll.get_length())
    ll.remove_at(3)
    ll.display()
    print('length : ', ll.get_length())
    ll.remove_at(1)
    ll.display()
    print('length : ', ll.get_length())
    ll.remove_at(0)
    ll.display()
    print('length : ', ll.get_length())
    ll.insert_at_begining('A')
    ll.insert_at_begining('B')
    ll.insert_at_begining('C')
    ll.display()
    print('length : ', ll.get_length())
    ll.remove_by_value('A')
    ll.display()
    print('length : ', ll.get_length())
    ll.insert_after_value(5, 8)
    ll.display()
    print('length : ', ll.get_length())

