from code_challenges.tree.tree import *


def test_empty_tree():
    tree = BinaryTree()
    assert tree.__str__() == 'This tree is empty'

# def test_one_node():
