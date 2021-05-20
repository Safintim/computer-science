from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder_traversal(root: TreeNode) -> List[int]:
    def traverse(root):
        if root:
            yield from traverse(root.left)
            yield root.val
            yield from traverse(root.right)

    return list(traverse(root))
