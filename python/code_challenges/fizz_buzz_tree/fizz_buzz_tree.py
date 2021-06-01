from tree import BinaryTree, TNode

class Empty_tree_exception(Exception):
	def __init__(self):
		pass

class Node():
	def __init__(self, value=None):
		self.value = value
		self.next = None


class Queue():
	def __init__(self):
		self.front = None
		self.rear = None
		self.length = 0

	def is_empty(self):
		if not self.front:
			return False
		return True

	def enqueue(self, value):
		if not self.is_empty():
			self.front = Node(value)
			self.rear = self.front
		else:
			new_node = Node(value)
			self.rear.next = new_node
			self.rear = new_node
		self.length += 1

	def dequeue(self):
		if not self.is_empty():
			raise Empty_tree_exception
		else:
			value = self.front.value
			self.front = self.front.next
			self.length -= 1
			return value

	def peek(self):
		if not self.is_empty():
			raise Empty_tree_exception
		else:
			return self.front.value

	def __str__(self):
		if not self.is_empty():
			raise Empty_tree_exception
		else:
			string = ""
			current = self.front
			while current != None:
				string += str(current.value) + ' '
				current = current.next
			return string

	def __len__(self):
		return self.length









def fizz_buzz_tree(Binary_tree):
  def fuzz_buzz(value):
      if value % 3 == 0 and value % 5 == 0:
          return 'FizzBuzz'
      elif value % 3 == 0:
          return "Fizz"
      elif value % 5 == 0:
          return "Buzz"
      else:
          return value


  root = Binary_tree.root
  new_root = TNode(root.value)
  new_tree = BinaryTree(new_root)
  if not new_root:
    raise Empty_tree_exception('Tree is EMPTY')
  roots = Queue()
  roots.enqueue(root)
  new_root.value = fuzz_buzz(new_root.value)
  new_rootsque = Queue()
  new_rootsque.enqueue(new_root)
  def inner_func(roots):
    for num in range(len(roots)):
      left = roots.peek().left
      right = roots.peek().right
      roots.dequeue()
      if left:
        new_left = TNode(fuzz_buzz(left.value))
        new_rootsque.peek().left = new_left
        roots.enqueue(left)
        new_rootsque.enqueue(new_left)
      if right:
        new_right = TNode(fuzz_buzz(right.value))
        new_rootsque.peek().right = new_right
        roots.enqueue(right)
        new_rootsque.enqueue(new_right)
      new_rootsque.dequeue()
    if len(roots) > 0:
      inner_func(roots)
  inner_func(roots)
  return new_tree






node1 = TNode(15)
node1.left = TNode(7)
node1.right = TNode(5)
node1.left.left = TNode(10)
node1.left.right = TNode(6)
node1.left.right.left = TNode(20)
node1.left.right.right = TNode(25)
node1.right.right = TNode(9)
node1.right.right.left = TNode(21)



binary_tree = BinaryTree(node1)



print(fizz_buzz_tree(binary_tree).in_order())
print(binary_tree.in_order())
