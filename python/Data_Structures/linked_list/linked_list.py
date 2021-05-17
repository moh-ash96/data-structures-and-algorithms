class Node():
    def __init__(self, value):
        self.value = value
        self.next = None




class Linked_list():
    def __init__(self):
         self.head = None

    def insert(self, val):
        '''
        inserts a value in front of the list
        '''
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node


    def includes(self, x):
        '''
        checks if the value provided is inside the list or not
        '''
        current = self.head
        try:
            while current != None:
                if current.value == x:
                    return True
                current = current.next
            return False
        except:
            print("Syntax Error")

    def __str__(self):
        '''
        returns a string of the list contents
        '''
        output = ''
        current = self.head
        try:
            while current:
                output += f"{ {current.value} }->"
                current = current.next
            output += f"{None}"
            return output
        except:
            print("Internal Error, Can't access list")

    def append(self, val):
        new_node = Node(val)

        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while (last.next):
            last = last.next

        last.next = new_node

    def insertAfter(self, val, new_value):

        if val is None:
            return print("The value to insert after is not in the Node")
        else:
            current = self.head
            new_node = Node(new_value)
            while current:
                if current.value == val:
                    new_node.next = current.next
                    current.next = new_node
                current = current.next

    def insertBefore(self, val, new_value):

        newNode = Node(new_value)

        current = self.head
        if current == None:
            return print('The linked list is empty')
        else:
            if current.value == val:
                newNode.next = self.head
                self.head = newNode

            while current.next:
                if current.next.value == val:
                    newNode.next = current.next
                    current.next = newNode
                    return
                else:
                    current = current.next
            print('The value to insert before is not in the Node')


    def kthFromEnd(self, k):
        current = self.head
        if current == None:
          return print('linked list is empty')

        if k < 0:
          return print("k should be a larger or equal to 0")

        length = 0
        while current is not None:
            current = current.next
            length += 1
        if k > length:
            print('kth is greater than the linked-list')
            return

        current = self.head
        for i in range(0, length - k - 1):
            current = current.next
        print(current.data)

    def empty_ll(self):
        self.head = None
        return

