
class Node:

	def __init__(self, d , next = None, prev = None):
		self.data = d
		self.next_node = next
		self.prev_node = prev

	def get_next(self):
		return self.next_node

	def set_next(self,next):
		self.next_node = next

	def get_prev(self):
		return self.prev_node

	def set_prev(self,prev):
		self.prev_node = prev

	def get_data(self):
		return self.data

	def set_data(self,d):
		self.data = d

"""
class Event:
    def __init__(self, time, event_type = None, next_event = None, prev_event = None):
        self.time = time
        self.event_type = event_type
        self.next_event = next_event
        self.prev_event = prev_event

	def get_next(self):
		return self.next_event

	def set_next(self,next):
		self.next_event = next

	def get_prev(self):
		return self.prev_event

	def set_prev(self,prev):
		self.prev_event = prev

	def get_time(self):
		return self.time

	def set_time(self,time):
		self.time = time

	def get_event_type(self):
		return self.event_type

	def set_event(self,event_type):
		self.event_type = event_type
"""

class DoublyLinkList(object):
	def __init__(self, d = None):
		self.head = d

	def isEmpty(self):
		return self.head is None	


	def add(self , d):
		new_node = Node(d)
		if self.head is None:
			self.head = new_node
		elif self.head.get_data > new_node.get_data:
			new_node.set_next(self.head)
			self.head.set_prev(new_node)
			self.head = new_node
		else:
			prev = self.head
			curr = self.head.get_next
			while curr is not None:
				if curr.get_data > new_node.get_data:
					prev.set_next(new_node)
					new_node.set_prev(prev)
					new_node.set_next(curr)
					curr.set_prev(new_node)
					return new_node
				prev = curr
				curr = curr.get_next

# Set current head to the next thing current head is poniting to. Ex. 1 -> 2 -> 3 -> 4 
# 1 is the head and it is pointing to 2. So you set the current header which is 1 to 2 so 
# it then removes 1.

	def remove():
		front = head
		if isEmpty:
			print("GEL is empty")
		else:
			head = head.get_next
		return front

		



		
		