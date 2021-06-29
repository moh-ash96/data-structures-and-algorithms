from Data_Structures.graph.graph import Graph
import pytest

def test_depth_question(depth):
    actual = []
    for node in depth[0].depth_first():
        actual.append(node.value)
    expected = ['A', 'B', 'C', 'G', 'D', 'E', 'H', 'F']
    assert actual == expected

def test_empty_graph():
    graph = Graph()
    actual = graph.depth_first()
    expected = []
    assert actual == expected

def test_trips_graph(depth):
    actual = []
    for node in depth[1].depth_first():
        actual.append(node.value)
    expected = ['Pandora', 'Arendelle', 'Metroville', 'Monstroplolis', 'Naboo', 'Narnia']
    assert actual == expected


@pytest.fixture
def depth():
    aj_list = Graph()
    a = aj_list.add_node('A')
    b = aj_list.add_node('B')
    c = aj_list.add_node('C')
    d = aj_list.add_node('D')
    e = aj_list.add_node('E')
    f = aj_list.add_node('F')
    g = aj_list.add_node('G')
    h = aj_list.add_node('H')
    aj_list.add_edge(a,b)
    aj_list.add_edge(a,d)
    aj_list.add_edge(b,c)
    aj_list.add_edge(b,d)
    aj_list.add_edge(c,g)
    aj_list.add_edge(d,e)
    aj_list.add_edge(d,h)
    aj_list.add_edge(d,f)
    aj_list.add_edge(h,f)

    g = Graph()
    node1 = g.add_node('Pandora')
    node2 = g.add_node('Arendelle')
    node3 = g.add_node('Metroville')
    node4 = g.add_node('Monstroplolis')
    node5 = g.add_node('Narnia')
    node6 = g.add_node('Naboo')

    g.add_edge(node1, node2, 150)
    g.add_edge(node1, node3, 82)
    g.add_edge(node2, node3, 99)
    g.add_edge(node2, node4, 42)
    g.add_edge(node3, node4, 105)
    g.add_edge(node3, node5, 37)
    g.add_edge(node3, node6, 26)
    g.add_edge(node4, node6, 73)
    g.add_edge(node5, node6, 250)
    return [aj_list, g]
