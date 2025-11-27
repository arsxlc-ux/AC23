class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None
def insert(root, key):
    if root is None:
        return TreeNode(key)
    if key < root.val:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root
def find_single_children(root, result=[]):
    if root is None:
        return
    if (root.left and not root.right) or (not root.left and root.right):
        result.append(root.val)
    find_single_children(root.left, result)
    find_single_children(root.right, result)
numbers = [7, 3, 2, 1, 9, 5, 4, 6, 8]
root = None
for num in numbers:
    root = insert(root, num)
single_children = []
find_single_children(root, single_children)
print(*sorted(single_children))

