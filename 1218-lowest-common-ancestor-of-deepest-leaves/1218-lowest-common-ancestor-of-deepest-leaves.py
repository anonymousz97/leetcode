from collections import deque

class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        queue = deque([(root, [root])])
        paths = []
        max_depth = 0

        while queue:
            node, path = queue.popleft()
            if not node.left and not node.right:
                if len(path) > max_depth:
                    max_depth = len(path)
                    paths = [path]
                elif len(path) == max_depth:
                    paths.append(path)
            if node.left:
                queue.append((node.left, path + [node.left]))
            if node.right:
                queue.append((node.right, path + [node.right]))

        lca = None
        for nodes in zip(*paths):
            if all(n == nodes[0] for n in nodes):
                lca = nodes[0]
            else:
                break

        return lca