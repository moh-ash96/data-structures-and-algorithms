class Node:
  def __init__(self, value=None):
    self.value = value
    self.next = None

class Stack:
  def __init__(self, node=None):
    self.top = node

  def push(self, value):
    if not self.top:
      self.top = Node(value)
    else:
      node = Node(value)
      node.next = self.top
      self.top = node

  def pop(self):
    if not self.is_empty():
      temp = self.top
      self.top = self.top.next
      temp.next = None
      return temp.value
    else:
        return 'Cannot pop from empty stack'

  def is_empty(self):
    if self.top:
      return False
    return True

  def peek(self):
    if not self.is_empty():
      return self.top.value

    return "Cannot peek from empty stack"



  def __str__(self):
    current = self.top
    items = []
    while current:
      items.append(str(current.value))
      current = current.next
    return "\n".join(items)



class PseudoQueue:
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def enqueue(self, value):

        current = self.s1.top

        while current:
            self.s2.push(current.value)
            current = current.next
            self.s1.pop()
        self.s1.push(value)
        current2 = self.s2.top
        while current2:
            self.s1.push(current2.value)
            current2 = current2.next
            self.s2.pop()


    def dequeue(self):
        if not self.s1.top:
            print("Queue is Empty")

        x = str(self.s1.top.value)
        self.s1.pop()
        return x

    def __str__(self):
        current = self.s1.top
        items = []
        while current:
            items.append(str(current.value))
            current = current.next
            print(current)
        return "\n".join(items)
