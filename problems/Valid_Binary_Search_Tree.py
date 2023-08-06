# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def dfs(node: TreeNode, lval, rval):
            if not node: return True
            if not(lval < node.val < rval):
                return False
            return dfs(node.left, lval, node.val) and dfs(node.right, node.val, rval)
        return dfs(root, float('-inf'), float('inf'))
        
# nonlocal ans
# if not node or not ans: return

# if node.left and ans:
#     if node.left.val >= lval or node.left.val >= node.val:
#         ans = False
#         return
#     dfs(node.left, min(lval,node.val), max(rval, node.val))
# if node.right and ans:
#     if node.right.val <= rval or node.right.val <= node.val:
#         ans = False
#         return
#     dfs(node.right, min(lval, node.val),max(rval,node.val))



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
x = insertLevelOrder([5,4,6,None,None,3,7],0)
# y = insertLevelOrder([4,1,2],0)

sol =Solution()
print(sol.isValidBST(x))