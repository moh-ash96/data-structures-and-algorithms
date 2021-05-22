from Data_Structures.linked_list.linked_list import Node, Linked_list
from Data_Structures.ll_zip.ll_zip import zipLists
import pytest

# @pytest.mark.skip
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
    actual = zipLists(ll1, ll2).__str__()
    expect = "{1}->{2}->{1}->{2}->{1}->{2}->{1}->{2}->None"
    assert actual == expect

def test_first_greater():
    llg = Linked_list()
    lll = Linked_list()

    llg.insert(2)
    llg.insert(3)
    llg.insert(1)

    lll.insert(9)
    lll.insert(5)

    assert zipLists(llg, lll) == "{1}->{5}->{3}->{9}->{2}->None"

def test_first_less():
    lll2 = Linked_list()
    llg2 = Linked_list()

    llg2.insert(4)
    llg2.insert(3)
    llg2.insert(1)

    lll2.insert(9)
    lll2.insert(5)

    assert zipLists(llg2, lll2) == "{1}->{5}->{3}->{9}->{4}->None"
