from Data_Structures.graph.linked_list import Linked_list, Node

class GNode():
    def __init__(self, value):
        self.value = value
        self.edges = []

    def __str__(self):
        return f"{self.value}"

class Graph():

    def __init__(self):
        self.nodes = []


    def add_node(self, value):
        node = GNode(value)
        lst = Linked_list()
        lst.head = node
        self.nodes.append(lst)
        return node



    def add_edge(self, node1, node2=None, weight = 1):
        first_list = None
        second_list = None
        if node2 == None:
            weight = 0

        if len(self.nodes) >0:
            for lst in self.nodes:
                if lst.head.value == node1:
                    first_list = lst
                elif lst.head.value == node2:
                    second_list = lst
            if first_list or second_list:
                if first_list:
                    if second_list:
                        first_list.head.edges.append([second_list.head,weight])
                    else:
                        first_list.head.edges.append([second_list,weight])
                if second_list:
                    if first_list:
                        second_list.head.edges.append([first_list.head,weight])
                    else:
                        second_list.head.edges.append([first_list,weight])


    def get_nodes(self):
        nodes = []
        if len(self.nodes)>0:
            for node in self.nodes:
                nodes.append(node.head.value)
            return nodes
        else:
            return None

    def get_neighbors(self, node_in):
        neighbors = []
        for node in self.nodes:
            if node.head.value == node_in:
                current = node.head
                neighbors.append(current.value)
                for edge in current.edges:
                    neighbors.append([str(edge[0]),edge[1]])
        return neighbors

    def size(self):
        return len(self.nodes)







if __name__ == '__main__':
    # ll = Linked_List()
    # ll.append(2)
    # ll.append(8)
    # ll.append(3)
    # ll.append(1)
    # ll.append(7)
    # ll.append(9)
    # ll.append(11)
    # ll.append(10)
    # print(ll)
    # for node in ll:
    #     print(node)
    aj_list = Graph()
    aj_list.add_node('a')
    aj_list.add_node('b')
    aj_list.add_node('c')
    aj_list.add_node('d')
    aj_list.add_node('e')
    aj_list.add_node('f')
    aj_list.add_edge('a','c')
    aj_list.add_edge('a','d')
    aj_list.add_edge('b','c')
    aj_list.add_edge('b','f')
    aj_list.add_edge('c','e')
    aj_list.add_edge('d','e')
    aj_list.add_edge('e','f')
    print(aj_list.get_nodes())
    print(aj_list.get_neighbors('a'))
    print(aj_list.get_neighbors('b'))
    print(aj_list.get_neighbors('c'))
    print(aj_list.get_neighbors('d'))
    print(aj_list.get_neighbors('e'))
    print(aj_list.get_neighbors('f'))
    print(aj_list.size())
