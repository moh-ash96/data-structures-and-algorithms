class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

# class Queue:
#     def __init__(self):
#         self.front = None
#         self.rear = None

#     def enqueue(self, value):
#         """ Add an item to the rear fo the queue """
#         node = Node(value)

#         if not self.front:
#             self.front = node
#             self.rear = node
#         else:
#             self.rear = self.rear.next

#     def dequeue(self):
#         temp = self.front
#         self.front = self.front.next
#         temp.next = None
#         return temp.value


class Cats:
    def __init__(self,value = "cat"):
        self.value = value
        self.next = None

class Dogs:
    def __init__(self,value = "dog"):
        self.value = value
        self.next = None

class AnimalShelter:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        """ Add an item to the rear fo the queue """
        if isinstance(value, Cats):
        # if value == 'cat':
            # cat = Queue()
            # cat.enqueue(value)
            node = Cats()
            # if not self.front:
            #     self.front = node
            #     self.rear = node

            # else:
            #     self.rear = self.rear.next
        elif isinstance(value, Dogs):
        # if value == 'dog':
            # dog = Queue()
            # dog.enqueue(value)
            node = Dogs()
        else:
            node = None

        if not self.front and node:
            self.front = node
            self.rear = self.front
        elif node:
            self.rear.next = node
            self.rear = node

    def __str__(self):
        current = self.front
        items = []
        while current:
            items.append(str(current.value))
            current = current.next
            # print(current)
        print(items)
        return "\n".join(items)



tom = Cats()
spike = Dogs()
shell = AnimalShelter()
shell.enqueue(tom)
shell.enqueue(spike)

print(shell.__str__())
