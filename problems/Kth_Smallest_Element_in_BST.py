# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        order = []
        def dfs(node: TreeNode):
            nonlocal order
            if not node: return
            dfs(node.left)
            order.append(node.val)
            dfs(node.right)
        dfs(root)
        return order[k-1]



def insertLevelOrder(arr, i):
    root = None
    # Base case for recursion 
    if i < len(arr):
        root = TreeNode(arr[i]) if arr[i] is not None else None
        # insert left child 
        if root:
            root.left = insertLevelOrder(arr, 2 * i + 1)
            # insert right child 
            root.right = insertLevelOrder(arr, 2 * i + 2)
    return root
x = insertLevelOrder([15,13,16,12,14,None,None,11],0)
# y = insertLevelOrder([4,1,2],0)

sol =Solution()
print(sol.kthSmallest(x, 6))