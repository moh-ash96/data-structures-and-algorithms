from Data_Structures.graph.graph import Graph
import pytest


def test_output(breadth):

    actual = breadth[0].breadth_first_search(breadth[1])
    expected = ['Pandora', 'Arendelle', 'Metroville', 'Monstroplolis', 'Naboo', 'Narnia']
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
