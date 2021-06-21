# import re
# def repeated_word(string):
#   li2 = string.split(' ')
#   li = []
#   for i in li2:
#     i = i.replace(',', '')
#     li.append(i.lower())
#   first_location = 0
#   second_location = 0
#   saved_word = ''
#   for word in li:
#     counter = 0
#     ind = 0
#     for i in li:
#       li2.append(i)
#     while word in li2:
#       if counter == 2:
#         break
#       ind = li2.index(word)
#       if ind is not None:
#         counter +=1
#         li2.pop(ind)
#     li2 = []
#     if counter == 2:
#       first_location = ind + counter

#       if first_location < second_location or second_location ==0:
#         second_location = first_location
#         saved_word = word

#   return saved_word

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


class Linked_list():
    def __init__(self):
        self.head = None
        self.length = 0

    def append(self, val):
        new_node = Node(val)

        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while (last.next):
            last = last.next

        last.next = new_node



class Hashtable():
    def __init__(self, size=1024):
        self.size = size
        self._buckets = [None]*size

    def _hash(self, key):
        sum = 0
        for char in key:
            sum += ord(char)
        hash_num = (sum * 29) % self.size
        return hash_num

    def add(self, key, value):
        index = self._hash(key)
        if not self._buckets[index]:
            self._buckets[index] = Linked_list()
        self._buckets[index].append([key, value])
        return [key, value]

    def contains(self, key):
        index = self._hash(key)
        bucket = self._buckets[index]
        if not bucket:
            return False
        else:
            current = bucket.head
            while current:
                if current.data[0] == key:
                    return True
                current = current.next



def repeated_word(string):
  word = ''
  linked = Linked_list()
  hash = Hashtable()
  for i in string:
    if i == ',':
      i = ''
    if i == ' ':
      linked.append(word.lower())
      word = ''
    else:
      word += i
  if word:
    linked.append(word.lower())
  current = linked.head
  while current:
    if hash.contains(current.data):
      return current.data
    else:
      hash.add(current.data, current.data)
    current = current.next

