from Data_Structures.graph.graph import Graph

def business_trip(graph, arr):
  try:
    total = 0
    def check_neighbors(city1, city2, graph):
      cost = 0
      node_li = []
      nodes = graph.get_nodes()
      for node in nodes:
        if city1 == node.value:
          node_li.append(node)

      node1 = node_li[0]
      for i in range(len(graph.get_neighbors(node1))):
        if city2 == graph.get_neighbors(node1)[i].vertex.value:
          cost += graph.get_neighbors(node1)[i].weight
      return cost

    for i in range(len(arr)-1):
      total += check_neighbors(arr[i], arr[i+1], graph)
    if total>0:
        return f'{total} $'
    else:
        return None
  except:
    return None
