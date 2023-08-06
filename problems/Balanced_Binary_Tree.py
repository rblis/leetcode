# Definition for a binary tree node.
import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        ans = True
        def dfs(node):
            nonlocal ans
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            if abs(left-right) > 1:
                ans = False
            return max(left,right)+1
        dfs(root)
        return ans


root = TreeNode(1,TreeNode(2,TreeNode(4,None, None), TreeNode(5,None,None)), TreeNode(3,None,None))

sol =Solution()
print(sol.isBalanced(root))