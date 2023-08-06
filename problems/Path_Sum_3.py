# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self) -> str:
        return str(self.val)
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        ans = 0
        paths = set()
        def dfs(node: TreeNode, val: int, path: set()):
            nonlocal ans, paths
            if val == targetSum and path not in paths:
                ans += 1
                paths.add(path)
            if not node:
                return
            path.add(node)
            dfs(node.left, val+node.val, path)
            dfs(node.right, val+node.val, path)
            path.pop(node)
            dfs(node.left, node.val, set(node))
            dfs(node.right, node.val, set(node))
        dfs(root,0, "")
        return ans

def insertLevelOrder(arr, i):
    root = None
    # Base case for recursion 
    if i < len(arr):
        root = TreeNode(arr[i]) if arr[i] != None else None
        if root:
            # insert left child 
            root.left = insertLevelOrder(arr, 2 * i + 1)
            # insert right child 
            root.right = insertLevelOrder(arr, 2 * i + 2)
    return root
x = insertLevelOrder([10,5,-3,3,3,None,11],0)
print(Solution().pathSum(x,8))