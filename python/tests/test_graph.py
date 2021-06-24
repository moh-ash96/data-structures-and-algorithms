from Data_Structures.graph.graph import Graph
import pytest

def test_add_node():
    graph = Graph()
    actual = graph.add_node('a')
    expected = 'a'
    assert expected == actual.value

def test_add_edge():
    graph = Graph()
    node1 = graph.add_node("a")
    node2 = graph.add_node("b")
    graph.add_edge(node1, node2)
    actual = graph.get_neighbors(node1)[0].vertex.value
    expected = "b"
    assert actual == expected

def test_get_nodes(graph):
    nodes = []
    for node in graph[0].get_nodes():
        nodes.append(node.value)
    actual = nodes
    expected = ['a','b','c','d','e','f']
    assert actual == expected

def test_neighbors(graph):
    lst = []
    for neighbor in graph[0].get_neighbors(graph[1]):
        lst.append(neighbor.vertex.value)
    actual = lst
    expected = ['c', 'd']
    assert actual == expected


def test_neighbors_with_weight(graph):
    lst = []
    for neighbor in graph[0].get_neighbors(graph[2]):
        lst.append([neighbor.vertex.value, neighbor.weight] )
    actual = lst
    expect = [['c', 0], ['f', [5]]]
    assert actual == expect


def test_size(graph):
    actual = graph[0].size()
    expected = 6
    assert actual == expected


def test_empty_graph():
    graph = Graph()
    actual = graph.get_nodes()
    expected = None
    assert actual == expected

@pytest.fixture
def graph():
    aj_list = Graph()
    node1 = aj_list.add_node('a')
    node2 = aj_list.add_node('b')
    node3 = aj_list.add_node('c')
    node4 = aj_list.add_node('d')
    node5 = aj_list.add_node('e')
    node6 = aj_list.add_node('f')
    aj_list.add_edge(node1,node3)
    aj_list.add_edge(node1,node4)
    aj_list.add_edge(node2,node3)
    aj_list.add_edge(node2,node6, [5])
    aj_list.add_edge(node3,node5)
    aj_list.add_edge(node4,node5)
    aj_list.add_edge(node5,node6)

    return [aj_list, node1, node2, node3, node4, node5, node6]
