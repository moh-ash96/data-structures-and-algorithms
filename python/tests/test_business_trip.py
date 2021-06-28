from code_challenges.business_trip.business_trip import business_trip, Graph
import pytest

def test_two_connected_cities(trip):
    actual = business_trip(trip, ['Metroville', 'Pandora'])
    expected = '82 $'
    assert actual == expected

def test_three_connected_cities(trip):
    actual = business_trip(trip, ['Arendelle', 'Monstroplolis', 'Naboo'])
    expected = '115 $'
    assert actual == expected

def test_disconnected_cities(trip):
    actual = business_trip(trip, ['Naboo', 'Pandora'])
    expected = None
    assert actual == expected

def test_separate_three_cities(trip):
    actual = business_trip(trip, ['Narnia', 'Arendelle', 'Naboo'])
    expected = None
    assert actual == expected

@pytest.fixture
def trip():
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
    return g
