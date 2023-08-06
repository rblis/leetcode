# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode:
        root = TreeNode(preorder[0])
        

print(Solution().buildTree(preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]))