from collections import deque

class Vertex():
    def __init__(self, value):
        self.value = value

    # def __str__(self):
    #     return f"{self.value}"

class Edge:
  def __init__(self, vertex, weight):
    self.vertex = vertex
    self.weight = weight

class Queue():
  def __init__(self):
    self.dq = deque()

  def enqueue(self, value):
    self.dq.appendleft(value)

  def dequeue(self):
    return self.dq.pop()

  def __len__(self):
    return len(self.dq)

class Stack():
  pass #we can use dq for that

class Graph():

    def __init__(self):
        self._adjacency_list = {}


    def add_node(self, value):
        v = Vertex(value)
        self._adjacency_list[v] = []
        return v



    def add_edge(self, start, end=None, weight = 0):

      if start not in self._adjacency_list:
        raise KeyError(f"Start vertex is not in the graph") #try concationation
      if end not in self._adjacency_list:
        raise KeyError("End vertex is not in the graph") # here too

      self._adjacency_list[start].append(Edge(end, weight))


    def get_nodes(self):
        if len(self._adjacency_list) > 0:
            return self._adjacency_list.keys()
        else:
            return None


    def get_neighbors(self, vertex):
      return self._adjacency_list.get(vertex, [])

    def size(self):
        return len(self._adjacency_list)


    def breadth_first_search(self, start_vertex, action=(lambda x: None)):
      queue = Queue()
      visited = set()
      queue.enqueue(start_vertex)
      visited.add(start_vertex)
      while len(queue):
        current_vertex = queue.dequeue()
        action(current_vertex)
        neighbors = self.get_neighbors(current_vertex)

        for edges in neighbors:
          neighbor_vertex = edges.vertex

          if neighbor_vertex in visited:
            continue

          else:
            visited.add(neighbor_vertex)
          queue.enqueue(neighbor_vertex)



