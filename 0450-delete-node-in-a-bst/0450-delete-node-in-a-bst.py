# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root:
            if key < root.val:
                root.left = self.deleteNode(root.left, key)
            elif key > root.val:
                root.right = self.deleteNode(root.right, key)
            else:
                if not root.left and not root.right:
                    return None
                if not root.left or not root.right:
                    return root.left if root.left else root.right
                tmp = TreeNode()
                tmp = root.left
                while tmp.right is not None:
                    tmp = tmp.right
                root.val = tmp.val
                root.left = self.deleteNode(root.left, tmp.val)
        return root