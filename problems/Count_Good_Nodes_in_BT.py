# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0
        def dfs(node: TreeNode, val):
            nonlocal ans
            if not node: return
            if node.val >= val:
                ans += 1
            dfs(node.left, max(val, node.val))
            dfs(node.right, max(val, node.val))
        dfs(root, root.val)
        return ans


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
x = insertLevelOrder([3,3,None,4,2],0)
# y = insertLevelOrder([4,1,2],0)

sol =Solution()
print(sol.goodNodes(x))