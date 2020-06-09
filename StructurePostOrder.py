from binaryTree import Tree, Node


def postOrderEx():
    tree = Tree()
    n1 = Node('A')  # I
    n2 = Node('M')  # N
    n3 = Node('A')  # S
    n4 = Node('Z')  # C
    n5 = Node('O')  # R
    n6 = Node('N')  # E
    n7 = Node(' ')
    n8 = Node(' ')
    n9 = Node('<')
    n0 = Node('3')

    n0.left = n6
    n0.right = n9
    n6.left = n1
    n6.right = n5
    n5.left = n2
    n5.right = n4
    n4.right = n3
    n9.left = n8
    n8.right = n7

    tree.root = n0

    return tree


if __name__ == "__main__":
    tree = postOrderEx()
    print('structure: ')

    tree.posOrder_traversal()
    print('         height:', tree.tree_height())
    # tree.inorder_traversal()

    # HOW To Run:  python3 structure.py
# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------
