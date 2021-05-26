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
        if value.lower() == 'cat':
            node = Cats()

        elif value.lower() == 'dog':
            node = Dogs()
        else:
            node = None

        if not self.front and node:
            self.front = node
            self.rear = self.front
        elif node:
            self.rear.next = node
            self.rear = node

    def dequeue(self, pref):
        animal = None
        if pref.lower() == 'dog' or pref.lower() == 'cat':
            temp = self.front.value
            if str(temp) == pref:
                animal = str(temp)
                self.front = self.front.next
            else:
                previous = self.front
                temp = previous
                while temp:
                    if str(temp.value) == pref:
                        dequeued = temp
                        animal = str(dequeued.value)
                        previous.next = dequeued.next
                        break
                    previous = temp
                    temp = temp.next
            return animal
        else:
            return animal


    def __str__(self):
        current = self.front
        items = []
        while current:
            items.append(str(current.value))
            current = current.next
        return "\n".join(items)

