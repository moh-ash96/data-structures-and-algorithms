from Data_Structures.graph.graph import Graph
import pytest


def test_output(breadth):
    li = []
    for node in breadth[0].breadth_first_traverse(breadth[1]):
        li.append(node.value)

    actual = li
    expected = ['Pandora', 'Arendelle', 'Metroville', 'Monstroplolis', 'Narnia', 'Naboo']
    assert actual == expected

def test_breadth_first_2(graph2):
    expected =  ['a', 'c', 'd', 'b', 'e', 'f']
    actual = []
    graph,node1 = graph2
    for node in graph.breadth_first_traverse(node1):
        actual.append(node.value)
    assert actual == expected

def test_breadth_first_3(graph3):
    expected =  ['a', 'Naboo', 'e', 'c', 'Arendelle', 'Metroville']
    actual = []
    graph,node1 = graph3
    for node in graph.breadth_first_traverse(node1):
        actual.append(node.value)
    assert actual == expected

@pytest.fixture
def breadth():
    g = Graph()
    node1 = g.add_node('Pandora')
    node2 = g.add_node('Arendelle')
    node5 = g.add_node('Narnia')
    node3 = g.add_node('Metroville')
    node4 = g.add_node('Monstroplolis')
    node6 = g.add_node('Naboo')

    g.add_edge(node1, node2)
    g.add_edge(node2, node3)
    g.add_edge(node3, node4)
    g.add_edge(node3, node5)
    g.add_edge(node3, node6)
    g.add_edge(node4, node6)
    g.add_edge(node5, node6)
    return [g, node1]

@pytest.fixture
def graph2():
    graph = Graph()
    node_a = graph.add_node('a')
    node_b = graph.add_node('b')
    node_c = graph.add_node('c')
    node_d = graph.add_node('d')
    node_e = graph.add_node('e')
    node_f = graph.add_node('f')
    graph.add_edge(node_a,node_c,1)
    graph.add_edge(node_a,node_d,3)
    graph.add_edge(node_b,node_c,5)
    graph.add_edge(node_b,node_f,7)
    graph.add_edge(node_c,node_e,9)
    graph.add_edge(node_d ,node_e,8)
    graph.add_edge(node_e,node_f,4)
    return graph,node_a


@pytest.fixture
def graph3():
    graph = Graph()
    node_a = graph.add_node('a')
    node_b = graph.add_node('Arendelle')
    node_c = graph.add_node('c')
    node_d = graph.add_node('Metroville')
    node_e = graph.add_node('e')
    node_f = graph.add_node('Naboo')
    graph.add_edge(node_a,node_f)
    graph.add_edge(node_b,node_e)
    graph.add_edge(node_c,node_d)
    graph.add_edge(node_e,node_a)
    graph.add_edge(node_f,node_b)
    graph.add_edge(node_a ,node_c)
    graph.add_edge(node_d,node_f)
    return graph,node_a
