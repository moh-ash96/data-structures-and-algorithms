from Data_Structures.linked_list.linked_list import Node, Linked_list
from Data_Structures.ll_zip.ll_zip import zipLists
import pytest

@pytest.mark.skip
def test_ll_zip():
    ll1 = Linked_list()
    ll2 = Linked_list()
    ll1.insert(1)
    ll1.insert(1)
    ll1.insert(1)
    ll1.insert(1)
    ll2.insert(2)
    ll2.insert(2)
    ll2.insert(2)
    ll2.insert(2)
    actual = zipLists(ll1, ll2)
    expect = "{1}->{2}->{1}->{2}->{1}->{2}->{1}->{2}->None"
    assert actual == expect
