from Data_Structures.hashtable.hashtable import Hashtable
from code_challenges.tree.tree import BinaryTree, TNode

def tree_insertion(binary1, binary2):
    arr = []
    tree1 = binary1.pre_order()
    tree2 = binary2.pre_order()
    hash = Hashtable()
    for root in tree1:
        hash.add(str(root), str(root))
    for root in tree2:
        if hash.contains(str(root)):
            arr.append(root)

    return arr


if __name__ == "__main__":
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

    binary_tree = BinaryTree(node1)

    binary_tree2 = BinaryTree(node2)

    print(tree_insertion(binary_tree, binary_tree2))







