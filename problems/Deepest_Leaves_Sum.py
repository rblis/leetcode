# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        ans = 0
        max_depth = float('-inf')
        def dfs(node, depth):
            nonlocal ans, max_depth
            if not node:
                return
            if not node.left and not node.right:
                if depth > max_depth:
                    max_depth = depth
                    ans = node.val
                elif depth == max_depth:
                    ans += node.val
            else:
                dfs(node.left, depth+1)
                dfs(node.right, depth+1)
        dfs(root, 0)
        return ans