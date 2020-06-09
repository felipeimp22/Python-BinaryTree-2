# exemple 1:
#     '10'
#    /    \
# '5'     '15'


# exemple 2:
#      '+'
#    /     \
#  'a'      '*'
#          /   \
#        'b'    '-'
#              /    \
#            '/'    'e'
#           /   \
#         'c'   'd'

# (a + (b * ((c/d) - e)))


# define the tree node


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# # return results as a string


    def __str__(self):
        return str(self.data)

# Define tree structure


class Tree:
    def __init__(self, data=None, node=None):
        if node:
            self.root = node
        elif data:
            node = Node(data)
            self.root = node
        else:
            self.root = None

    # percurso em ordem simetrica

    def inorder_traversal(self, node=None):
        if node is None:
            node = self.root

        if node.left:
            # print('dd', end='')

            self.inorder_traversal(node.left)
            # o end= no final do print serve para o python nao pular linha no print
        print(node, end=" \n ")

        if node.right:

            self.inorder_traversal(node.right)
            # print('', end='')

    def posOrder_traversal(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            self.posOrder_traversal(node.left)
        if node.right:
            self.posOrder_traversal(node.right)
        print(node, end="")

    def tree_height(self, node=None):
        if node is None:
            node = self.root
        hLeft = 0
        hRight = 0
        if node.left:
            hLeft = self.tree_height(node.left)
        if node.right:
            hRight = self.tree_height(node.right)
        if hRight > hLeft:
            return hRight + 1
        return hLeft + 1


class binarySearchTree(Tree):
    def insert(self, value):
        parent = None
        x = self.root
        while(x):
            parent = x
            if value < x.data:
                x = x.left
            else:
                x = x.right
        if parent is None:
            self.root = Node(value)
        elif value < parent.data:
            parent.left = Node(value)
        else:
            parent.right = Node(value)

    # standart value
    # def search(self, value, node=0):
    #     if node == 0:
    #         node = self.root
    #     if node is None or node.data == value:
    #         return Tree(node)
    #     if value < node.data:
    #         return self.search(value, node.left)
    #     return self.search(value, node.right)

    def search(self, value):
        return self._search(value, self.root)

    def _search(self, value, node):
        if node is None:
            return node
        if node.data == value:
            return Tree(node)
        if value < node.data:
            return self._search(value, node.left)
        return self._search(value, node.right)
