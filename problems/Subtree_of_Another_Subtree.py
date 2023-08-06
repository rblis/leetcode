# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        if self.check(root, subRoot): #check using root as base
            return True
        elif root is None:
            return False
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot) #check down the children for subtree
    
    def check(self, root: TreeNode, sub:TreeNode):
        
        if (root is None) ^ (sub is None): #either one of them is None
            return False
        elif root is None and sub is None:
            return True

        
        if root.val == sub.val:
            if self.check(root.left, sub.left) and self.check(root.right, sub.right): #checks node by node until both nodes are NULL
                return True
            else:
                return False
        else:
            return False
    
    def dfs(self, node: TreeNode, res: list[int], cet: set):
        if node == None:
            return 
        res.append(node.val)
        self.dfs(node.left, res)
        self.dfs(node.right, res)
        return res

