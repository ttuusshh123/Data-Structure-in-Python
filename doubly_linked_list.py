class Node:
	def __init__(self, data):
		self.data = data
		self.prev = None
		self.next = None

	def __str__(self):
		return "data->{}".format(self.data)

class DoublyLinkedList:
	def __init__(self):
		self.head = None

	def add_last(self, data):
		n = Node(data)
		if self.head == None:
			self.head = n
		else:
			p = self.head
			while p.next != None:
				p = p.next
			n.prev = p
			p.next = n

	def add_first(self,data):
		n = Node(data)
		if self.head == None:
			self.head = None
		else:
			n.next = self.head

	def list_to_dll(self, l):
		if self.head != None:
			raise Exception("you cannot create dll")
		else:
			for i in l:
				self.add_last(i)





	def display(self):
		if self.head == None:
			print("Empty")
		else:
			p = self.head
			c = 1
			while p:
				# print(f"head value->{self.head.data} and node value is {p.data}")
				print(f"{c}th node is {p.data}")
				p = p.next
				c+=1

	def size_dll(self):
		if self.head == None:
			return 0
		else:
			p = self.head
			count = 0
			while p:
				p = p.next
				count += 1
			return count



	def delete_node(self, index):
		#index starts from 0
		if self.head == None:
			raise Exception("List is Empty, you cannot delete Node")
		else:
			if self.size_dll() <= index:
				raise Exception("check your index and size of dll")
			else:
				if index == 0:
					temp = self.head.data
					self.head.next.prev = self.head
					self.head = self.head.next
					return temp
				elif index == (self.size_dll()-1):
					p = self.head
					q = None
					while p.next != None:
						q = p
						p = p.next
					q.next = None

				else:
					p = self.head
					q = None
					for i in range(index):
						q = p
						p = p.next
					temp = p.data
					p.next.prev = q
					q.next = p.next
					return temp

	def delete_last_node(self):
		try:
			if self.head == None:
				raise Exception("No element to delete")
			else: 		
				p = self.head
				while p.next != None:
					p = p.next
				p.prev.next = None
		except Exception as e:
			print("you cannot delete element from an empty dll")

	def delete_first_node(self):
		if self.head == None:
			print("list is empty")
		else:
			self.head = self.head.next










dll = DoublyLinkedList()

dll.list_to_dll([23,53,98,32,748,99,33])

dll.display()
print("\n")
dll.delete_first_node()
# print(dll.size_dll())
# print("after")
dll.display()
# print("\n")
# dll.delete_node(1)
# dll.display()



