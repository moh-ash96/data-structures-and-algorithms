import pytest
from code_challenges.tree.tree import *

def test_breadth_first(binary):
    actual = binary.breadth_first(binary)
    expect = [2, 7, 5, 2, 6, 9, 5, 11, 4]
    assert actual == expect


def test_empty_tree():
    tree = BinaryTree()
    with pytest.raises(Empty_tree_exception):
        tree.find_maximum_value()




@pytest.fixture
def binary():
    node1 = TNode(2)
    node1.left = TNode(7)
    node1.right = TNode(5)
    node1.left.left = TNode(2)
    node1.left.right = TNode(6)
    node1.left.right.left = TNode(5)
    node1.left.right.right = TNode(11)
    node1.right.right = TNode(9)
    node1.right.right.left = TNode(4)
    tree = BinaryTree(node1)
    return tree
