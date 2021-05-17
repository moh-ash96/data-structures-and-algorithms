import pytest

from Data_Structures.linked_list.linked_list import Node, Linked_list


def test_import():
    assert Linked_list


l_list = Linked_list()


def test_empty():
    actual = l_list.head
    expect = None
    assert actual == expect


def test_insert():
    l_list.insert(5)
    actual = l_list.includes(5)
    expect = True
    assert actual == expect


def test_head():
    l_list.insert(5)
    l_list.insert(10)
    l_list.insert(18)
    actual = l_list.head.value
    expect = 18
    assert actual == expect
    actual2 = l_list.head.next.value
    expect2 = 10
    assert actual2 == expect2


def test_true_false():
    actual = l_list.includes(10)
    expect = True
    assert actual == expect
    actual2 = l_list.includes(7)
    expect2 = False
    assert actual2 == expect2


def test_return():
    actual = l_list.__str__()
    expect = "{18}->{10}->{5}->{5}->None"
    assert actual == expect


def test_append():
    l_list.append(8)
    actual = l_list.__str__()
    expect = "{18}->{10}->{5}->{5}->{8}->None"
    assert actual == expect


def test_insert_after():
    l_list.insertAfter(10, 6)
    actual = l_list.__str__()
    expect = "{18}->{10}->{6}->{5}->{5}->{8}->None"
    assert actual == expect


def test_insert_before():
    l_list.insertBefore(6, 20)
    actual = l_list.__str__()
    expect = "{18}->{10}->{20}->{6}->{5}->{5}->{8}->None"
    assert actual == expect

@pytest.mark.skip
def test_kth_from_end():
    actual = l_list.kthFromEnd(5)
    expect = 10
    assert actual == expect

@pytest.mark.skip
def test_k_is_greater_than_list_length():
    actual = l_list.kthFromEnd(10)
    expect = 'kth is greater than the linked-list'
    assert actual == expect

@pytest.mark.skip
def test_k_and_len_are_the_same():
    actual = l_list.kthFromEnd(7)
    expect = 18
    assert actual == expect

@pytest.mark.skip
def test_negative_value():
    actual = l_list.kthFromEnd(-1)
    expect = 'k should be a larger or equal to 0'
    assert actual == expect

@pytest.mark.skip
def test_empty_ll():
    l_list.empty_ll()
    actual = l_list.kthFromEnd(1)
    expect = "linked list is empty"
    assert actual == expect

@pytest.mark.skip
def test_linked_list_one_node():
    l_list.insert(1)
    actual = l_list.kthFromEnd(0)
    expect = 1
    assert actual == expect

