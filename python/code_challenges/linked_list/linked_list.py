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

