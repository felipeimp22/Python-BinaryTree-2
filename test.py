import random
from binaryTree import binarySearchTree

random.seed(77)  # to generate same numbers sequences

values = random.sample(range(1, 1000), 42)

bst = binarySearchTree()

for i in values:
    bst.insert(i)

bst.inorder_traversal()

items = [1, 3, 981, 510, 1000]
for item in items:
    r = bst.search(item)
    if r is None:
        print(item, "não encontrado")
    else:
        print(r.root.data, "encontrado")
