class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth(self, root: TreeNode) -> int:
    def traverse(root, level):
        if not root:
            return level
        return max(traverse(root.left, level + 1), traverse(root.right, level + 1))
    return traverse(root, 0)
