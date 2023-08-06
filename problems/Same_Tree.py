# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        ans = True
        def dfs(a: TreeNode,b: TreeNode):
            nonlocal ans
            if not a and not b:
                return
            if not a or not b or a.val != b.val:
                ans = False
                return
            if not ans: return
            dfs(a.left, b.left)
            if not ans: return
            dfs(a.right, b.right)
        dfs(p,q)
        return ans

x = TreeNode(1,TreeNode(2,TreeNode(4,None, None), TreeNode(5,None,None)), TreeNode(3,None,None))
y = TreeNode(1,TreeNode(2,TreeNode(4,None, None), TreeNode(5,None,None)), TreeNode(3,None,None))

def insertLevelOrder(arr, i):
    root = None
    # Base case for recursion 
    if i < len(arr):
        root = TreeNode(arr[i])   
        # insert left child 
        root.left = insertLevelOrder(arr, 2 * i + 1)
        # insert right child 
        root.right = insertLevelOrder(arr, 2 * i + 2)
    return root

sol =Solution()
print(sol.isSameTree(x,y))