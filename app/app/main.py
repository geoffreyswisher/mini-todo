import sys

from Stack import Stack





def errorCheck(error):
	retstr = 'Error: '

	x, y = error.args

	if x == 'Index Error':
		if y == '<':
			retstr += 'Index value too small\n'
		if y == '>':
			retstr += 'Index value too large\n'

	return retstr


def load(filename):
	file = open(filename, 'r')
	
	if not file:
		return -1

	larray = []

	for line in file.readlines():
		larray.append(line.strip())

	lstack = Stack(larray, len(larray))

	file.close()

	return lstack

def save(stack, filename):
	file = open(filename, 'w')

	for item in stack.toArray():
		file.write(str(item) + '\n')

	file.close()


def _help(stack, args):
	print('Help Menu')
	print('Actions:')
	print('1)  list                ---  displays all items in your todo list (done by default with every action)' )
	print('2)  add [item]          ---  adds item to the end(bottom) of the list')
	print('3)  add [item] [place]  ---  adds item to a specific place in the list')
	print('4)  remove              ---  removes the last(bottom) item in the list')
	print('5)  remove [place]      --- removes the item in the specific place in the list; all items below shift up')
	print('6)  clear               ---  removes all items from the list')

def display(stack, args):
	print("Your todo list:")

	for _,item in enumerate(stack.toArray()):
		print("%d)	%s" % (_+1,item))

def add(stack, args):
	if len(args) == 1:
		stack.push(args[0])

	if len(args) == 2:
		try:
			stack.insert(int(args[1]) - 1, args[0])
		except Exception as e:
			print(errorCheck(e))

def remove(stack, args):
	if len(args) == 0:
		try:
			stack.popLast()
		except Exception as e:
			print(errorCheck(e))

	if len(args) == 1:
		stack.pop(int(args[0]) - 1)

def clear(stack, args):
	stack.clear()

switch = {
	'list': display,
	'add': add,
	'remove': remove,
	'clear': clear,
	'help': _help
}

def main():

	filepath = sys.argv[1]

	try:
		stack = load(filepath)
	except:
		print('Save file does not currently exist. Normal for first-time use.')
		stack = Stack()

	args = sys.argv[2::]

	if len(args) < 1:
		print('Too few arguments.')
		print('Usage is "$ todolist [action] [arguments]"')
		print('Use action "help" to list actions and their arguments\n')
		return -1

	func = switch.get(args[0])

	try:
		func(stack, args[1::])
	except Exception as e:
		print(e)
		print('Invalid command')
		print('Usage is "$ todolist [action] [arguments]"')
		print('Use action "help" to list actions and their arguments\n')

	display(stack, args[1::])

	save(stack, filepath)




main()


# Bash Script
# 	check python
#	mkdir /opt/user/todolist
