# from python.code_challenges.tree.tree import BinaryTree, TNode
# from python.code_challenges.tree.tree import BinaryTree, Empty_tree_exception
import pytest
from code_challenges.tree.tree import *

def test_maximum_tree(binary):
    actual = binary.find_maximum_value()
    expect = 11
    assert actual == expect


def test_empty_tree():
    tree = BinaryTree()
    with pytest.raises(Empty_tree_exception):
        tree.find_maximum_value()




@pytest.fixture
def binary():
    node = TNode(2)
    node.left = TNode(7)
    node.right = TNode(5)
    node.left.left = TNode(2)
    node.left.right = TNode(6)
    node.left.right.left = TNode(5)
    node.left.right.right = TNode(11)
    node.right.right = TNode(9)
    node.right.right.left = TNode(4)
    tree = BinaryTree(node)
    return tree


