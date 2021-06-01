from code_challenges.fizz_buzz_tree.fizz_buzz_tree import fizz_buzz_tree
from code_challenges.tree.tree import TNode, BinaryTree
import pytest

def test_fizz_buzz(binary):
    actual = fizz_buzz_tree(binary).in_order()
    expect = ['Buzz', '7', 'Buzz', 'Fizz', 'Buzz', 'FizzBuzz', 'Buzz', 'Fizz', 'Fizz']
    assert actual == expect









@pytest.fixture
def binary():
    node1 = TNode(15)
    node1.left = TNode(7)
    node1.right = TNode(5)
    node1.left.left = TNode(10)
    node1.left.right = TNode(6)
    node1.left.right.left = TNode(20)
    node1.left.right.right = TNode(25)
    node1.right.right = TNode(9)
    node1.right.right.left = TNode(21)
    tree = BinaryTree(node1)
    return tree
