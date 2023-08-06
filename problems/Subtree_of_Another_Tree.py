# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, root:TreeNode, subRoot:TreeNode) -> bool:
        ans = False
        def sameTree(a: TreeNode,b: TreeNode):
            if not a and not b:
                return True
            if not a or not b or a.val != b.val:
                return False
            return sameTree(a.left, b.left) and sameTree(a.right, b.right)
        def dfs(node):
            nonlocal ans
            if not node or ans: return 
            if node.val == subRoot.val and sameTree(node, subRoot):
                ans = True
            if not ans:
                dfs(node.left)
            if not ans:
                dfs(node.right)
        dfs(root)
        return ans

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
x = insertLevelOrder([3,4,5,1,2],0)
y = insertLevelOrder([4,1,2],0)

sol =Solution()
print(sol.isSubtree(x,y))