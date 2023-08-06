# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        ans = 0
        def dfs(node, depth):
            nonlocal ans
            if not node:
                return depth-1
            left = dfs(node.left, depth + 1)
            right = dfs(node.right, depth+1)
            ans = max(ans, left+right-(2*depth))
            return max(left,right)
        dfs(root, 0)
        return ans    

root = TreeNode(1,TreeNode(2,TreeNode(4,None, None), TreeNode(5,None,None)), TreeNode(3,None,None))

sol =Solution()
print(sol.diameterOfBinaryTree(root))