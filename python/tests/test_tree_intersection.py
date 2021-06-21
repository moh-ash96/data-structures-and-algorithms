from code_challenges.tree_intersection.tree_intersection import tree_intersection, BinaryTree, TNode
import pytest

def test_tree_intersection(intersection):

    actual = tree_intersection(intersection[0], intersection[1])
    expected = [100,160,125,175,200,350,500]
    assert actual == expected

def test_no_intersections(intersection):
    actual = tree_intersection(intersection[2], intersection[3])
    expected = 'There are no intersections'
    assert actual == expected




@pytest.fixture
def intersection():
    node1 = TNode(150)
    node1.left = TNode(100)
    node1.left.left = TNode(75)
    node1.left.right = TNode(160)
    node1.left.right.left = TNode(125)
    node1.left.right.right = TNode(175)
    node1.right = TNode(250)
    node1.right.left = TNode(200)
    node1.right.right = TNode(350)
    node1.right.right.left = TNode(300)
    node1.right.right.right = TNode(500)

    node2 = TNode(42)
    node2.left = TNode(100)
    node2.left.left = TNode(15)
    node2.left.right = TNode(160)
    node2.left.right.left = TNode(125)
    node2.left.right.right = TNode(175)
    node2.right = TNode(600)
    node2.right.left = TNode(200)
    node2.right.right = TNode(350)
    node2.right.right.left = TNode(4)
    node2.right.right.right = TNode(500)

    node3 = TNode(5)
    node3.right = TNode(6)
    node3.left = TNode(7)
    node3.right.left = TNode(9)
    node3.left.left = TNode(50)

    node4 = TNode(11)
    node4.right = TNode(12)
    node4.left = TNode(13)
    node4.right.left = TNode(14)
    node4.left.left = TNode(15)

    binary_tree = BinaryTree(node1)
    binary_tree2 = BinaryTree(node2)

    binary_tree3 = BinaryTree(node3)
    binary_tree4 = BinaryTree(node4)

    return [binary_tree, binary_tree2, binary_tree3, binary_tree4]
