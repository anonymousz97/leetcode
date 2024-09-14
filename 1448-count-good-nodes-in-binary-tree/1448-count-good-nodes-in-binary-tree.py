# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        cnt = 0
        def dfs(root, max_vl):
            nonlocal cnt
            if root is None:
                return 
            if root.left is None and root.right is None:
                if root.val > max_vl:
                    cnt += 1
                    # print(root, cnt)
                    return
            if root.val >= max_vl:
                cnt += 1
                max_vl = root.val
                # print(root, cnt)
            dfs(root.left, max_vl)
            dfs(root.right, max_vl)
        
        dfs(root, root.val)
        return cnt
        