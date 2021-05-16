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

    def insertAfter(self, value, new_value):

        if value is None:
            print("The value to put after is not in the Node")
            return
        else:
            current = self.head
            new_node = Node(new_value)
            while current:
                if current.data == value:
                    new_node.next = current.next
                    current.next = new_node
                current = current.next



