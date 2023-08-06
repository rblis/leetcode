# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self) -> str:
        return str(self.val)
class Solution:
    def rob(self, root: TreeNode) -> int:
        def dfs(node: TreeNode):
            if not node: return (0,0)
            left, right = dfs(node.left), dfs(node.right)
            rob_root = node.val + left[1]+right[1]
            rob_child = max(left) + max(right)
            return (rob_root, rob_child)
        return max(dfs(root))

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
x = insertLevelOrder([4,1],0)

print(Solution().rob(x))