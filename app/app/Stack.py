class Stack:

	def __init__(self, stack=[], size=0):
		self.stack = stack
		self.size = size



	def push(self, item):
		self.stack.append(item)
		self.size += 1
		return True

	def insert(self, place, item):
		if place > self.size:
			raise Exception('Index Error', '>')
			return -1
		if place < 0:
			raise Exception('Index Error', '<')
			return -1

		self.stack.insert(place, item)
		self.size += 1
		return True

	def popLast(self):
		return self.pop(self.size - 1)
		
	def popFirst(self):
		return self.pop(0)

	def pop(self, place):
		if place >= self.size:
			raise Exception('Index Error', '>')
			return -1
		if place < 0:
			raise Exception('Index Error', '<')
			return -1

		val = self.stack.pop(place)
		self.size -= 1
		return val

	def clear(self):
		self.stack = []
		self.size = 0


	def toArray(self):
		return self.stack

	def getSize(self):
		return self.size

	def getItem(self, place):
		return self.stack[place]

	def getFirst(self):
		return self.stack[0]

	def getLast(self):
		return self.stack[self.size - 1]

