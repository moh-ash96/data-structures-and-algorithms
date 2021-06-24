class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
        else:
            current =self.head
            while current.next:
                current = current.next
                current.next = node

    def __iter__(self):
        current= self.head
        while current:
            yield current.value
            current = current.next

class Hashtable():
    def __init__(self, size=1024):
        self.size = size
        self._buckets = [None]*size
        self.keys = []

    def _hash(self, key):
        sum = 0
        for char in key:
            sum += ord(char)
        hash_num = (sum * 29) % self.size
        return hash_num

    def add(self, key, value):
        index = self._hash(key)
        if not self._buckets[index]:
            self._buckets[index] = LinkedList()
        self._buckets[index].append([key, value])
        self.keys.append(key)
        return [key, value]

    def get(self, key):
        index = self._hash(key)
        bucket = self._buckets[index]

        if not bucket:
            return None
        else:
            current = bucket.head

            while current:
                if current.value[0] == key:
                    return current.value[1]
                current = current.next

    def contains(self, key):
        index = self._hash(key)
        bucket = self._buckets[index]
        if not bucket:
            return False
        else:
            current = bucket.head
            while current:
                if current.value[0] == key:
                    return True
                current = current.next

    # def entries(self):
    #     lst = []
    #     for bucket in self._buckets:
    #         if bucket:
    #             for node in bucket:
    #                 lst.append(node)
    #     return lst

    # def keys(self):
    #     lst = []
    #     for entry in self.entries():
    #         lst.append(entry[0])
    #     return lst
