from abc import ABC
from Data_Structures.graph.graph import Graph
import pytest

def test_add_node():
    graph = Graph()
    actual = str(graph.add_node('a'))
    expected = 'a'
    assert actual == expected

def test_add_edge():
    graph = Graph()
    graph.add_node("a")
    graph.add_node("b")
    graph.add_edge("a", "b")
    edge = graph.nodes[0].head.edges[0]
    actual = [str(edge[0]), edge[1]]
    expected = ['b', 1]
    assert actual == expected

def test_get_nodes(graph):
    actual = graph.get_nodes()
    expected = ['a','b','c','d','e','f']
    assert actual == expected

def test_neighbors(graph):
    actual = graph.get_neighbors('a')
    expected = ['a', ['c', 1], ['d', 1]]
    assert actual == expected


def test_neighbors_with_weight(graph):
    actual = graph.get_neighbors('b')
    expect = ['b', ['c', 1], ['f', 5]]
    assert actual == expect


def test_size(graph):
    actual = graph.size()
    expected = 6
    assert actual == expected

def test_one_node():
    graph = Graph()
    graph.add_node('a')
    graph.add_edge('a')
    actual = graph.get_neighbors('a')
    expect = ['a', ['None', 0]]
    assert actual == expect


def test_empty_graph():
    graph = Graph()
    actual = graph.get_nodes()
    expected = None
    assert actual == expected

@pytest.fixture
def graph():
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
    aj_list.add_edge('b','f', 5)
    aj_list.add_edge('c','e')
    aj_list.add_edge('d','e')
    aj_list.add_edge('e','f')

    return aj_list
