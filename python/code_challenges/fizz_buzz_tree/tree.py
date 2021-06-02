class Empty_tree_exception(Exception):
    def __init__(self):
        pass

class TNode:
  def __init__(self, value=None):
    self.value = value
    self.left = None
    self.right = None

class BinaryTree:
    def __init__(self, root=None):
        self.root = root
        self.tree_list = []


    def pre_order(self):
        self.tree_list = []
        """ Pre-order traversal of our tree """
        def walk(root):
            self.tree_list.append(root.value)

            if root.left:
                walk(root.left)

            if root.right:
                walk(root.right)

        walk(self.root)
        return self.tree_list



    def in_order(self):
        self.tree_list = []
        """ in-order traversal of our tree """
        def walk(root):

            if root.left:
                walk(root.left)
            self.tree_list.append(root.value)

            if root.right:
                walk(root.right)

        walk(self.root)
        return self.tree_list


    def post_order(self):
        self.tree_list = []
        """ in-order traversal of our tree """
        def walk(root):

            if root.left:
                walk(root.left)

            if root.right:
                walk(root.right)

            self.tree_list.append(root.value)
        walk(self.root)
        return self.tree_list


    def find_maximum_value(self):
        def max(arr):
            current = arr[0]
            for i in arr:
                if i > current:
                    current=i
            return current
        if not self.root:
            raise Empty_tree_exception
        else:
            my_list = self.pre_order()
        return max(my_list)

    # def breadth_first(self, b_tree):
    #     roots = []
    #     root = b_tree.root
    #     self.tree_list = []
    #     self.tree_list.append(roots[0].value)
    #     def inner_function(roots):
    #         for root in roots:
    #             left = root.left
    #             right = root.right
    #             self.tree_list.append(root.left)
    #             roots.append(left)
    #             self.tree_list.append(root.right)
    #             roots.append(right)

    def breadth_first(self, b_tree):

        if b_tree.root is None:
            raise Exception('Tree is empty')

        queue = []
        output = []

        queue.append(b_tree.root)

        while(len(queue) > 0):

            output.append(queue[0].value)
            node = queue.pop(0)

            if node.left is not None:
                queue.append(node.left)

            if node.right is not None:
                queue.append(node.right)
        return output




    def __str__(self):

        items = []

        if self.tree_list == []:
            return 'This tree is empty'
        else:
            for i in self.tree_list:
                items.append(str(i))
        return '\n'.join(items)


class Binary_search_tree:
    def __init__(self, root=None):
        self.root = root
        self.tree_list = []
        self.val = False

    def add(self, value, root=None):
        self.tree_list = []
        def inner_function(value, root=None):
            if not self.root:
                self.root = TNode(value)
            elif not root:
                inner_function(value, self.root)

            else:
                self.tree_list.append(root.value)
                if value < root.value:
                    if not root.left:
                        root.left = TNode(value)
                        self.tree_list.append(root.left.value)
                    else:
                        inner_function(value, root.left)
                if value > root.value:
                    if not root.right:
                        root.right = TNode(value)
                        self.tree_list.append(root.right.value)
                    else:
                        inner_function(value, root.right)
        inner_function(value)
        return self.tree_list




    def contains(self, value, root=None):
        if not self.root:
            raise Exception('Tree is empty')
        elif not root:
            self.contains(value, self.root)

        else:
            if value == root.value:
                self.val = True
            if value < root.value:
                if not root.left:
                    self.val = False
                else:
                    self.contains(value, root.left)
            if value > root.value:
                if not root.right:
                    self.val = False
                else:
                    self.contains(value, root.right)

        return self.val

    def __str__(self):

        items = []

        if self.tree_list == []:
            return 'This tree is empty'
        else:
            for i in self.tree_list:
                items.append(str(i))
        return '\n'.join(items)






# if __name__ == "__main__":


#   node1 = TNode('A')
#   node1.left = TNode('B')
#   node1.right = TNode('C')
#   node1.left.left = TNode('D')
#   node1.left.right = TNode('E')
#   node1.right.left = TNode('F')



#   binary_tree = BinaryTree(node1)

#   tree = Binary_search_tree()
#   print(tree.add(23))
#   print(tree.add(8))
#   print(tree.add(42))
#   print(tree.add(4))
#   print(tree.add(16))
#   print(tree.add(27))
#   print(tree.add(85))
#   print(tree.add(15))
#   print(tree.add(22))
#   print(tree.add(105))

#   print(tree.contains(23))
#   print(tree.contains(8))
#   print(tree.contains(42))
#   print(tree.contains(4))
#   print(tree.contains(16))
#   print(tree.contains(27))
#   print(tree.contains(85))
#   print(tree.contains(15))
#   print(tree.contains(22))
#   print(tree.contains(105))

#   print('go to wrong')

#   # print(tree.contains(23))
#   print(tree.contains(7))
#   print(tree.contains(40))
#   print(tree.contains(3))
#   print(tree.contains(106))
#   print(tree.contains(50))
#   print(tree.contains(65))
#   print(tree.contains(10))
#   print(tree.contains(78))
#   print(tree.contains(90))


#   print(binary_tree.pre_order())
#   print(binary_tree.in_order())
#   print(binary_tree.post_order())
#   # binary_tree.pre_order_iter()




# # Think about
# class KNode:
#   def __init__(self, value=None):
#     self.value = value
#     # How could you implement this for k of any size?
#     self.children = []
