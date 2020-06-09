from binaryTree import Tree, Node


def inOrderEx():

    tree = Tree()

    n1 = Node("T")
    n2 = Node("H")
    n3 = Node("N")
    n4 = Node("A")
    n5 = Node("U")
    n6 = Node("Y")
    n7 = Node("K")
    n8 = Node("O")

    n6.left = n7
    n6.right = n8

    n5.left = n6

    n3.left = n4
    n3.right = n5

    n2.left = n1
    n2.right = n3

    tree.root = n2

    return tree


if __name__ == "__main__":
    tree = inOrderEx()
    print('structure: ')

    tree.inorder_traversal()

    # HOW To Run:  python3 structure.py
# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------
