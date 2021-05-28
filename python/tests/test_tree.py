from code_challenges.tree.tree import *


def test_empty_tree():
    tree = BinaryTree()
    assert tree.__str__() == 'This tree is empty'

def test_one_node():
    node = TNode('5')

    tree = BinaryTree(node)

    assert tree.pre_order() == ['5']

def test_add_lef_right():
    node = TNode('5')
    node.right = TNode('15')
    node.left = TNode('10')

    tree = BinaryTree(node)

    assert tree.pre_order() == ['5', '10', '15']


node = TNode('1')
node.left = TNode('2')
node.right = TNode('5')
node.left.left = TNode('3')
node.left.right = TNode('4')
node.right.left = TNode('6')
node.right.right = TNode('7')

tree = BinaryTree(node)

def test_pre_order():

    assert tree.pre_order() == ['1', '2', '3', '4', '5', '6', '7']


def test_in_order():
    assert tree.in_order() == ['3', '2', '4', '1', '6', '5', '7']

def test_post_order():
    assert tree.post_order() == ['3', '4', '2', '6', '7', '5', '1']
