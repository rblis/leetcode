# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> list[int]:
        ans = []
        if not root:
            return ans
        ans.append(root.val)
        def dfs(node: TreeNode, depth: int):
            nonlocal ans
            if node.right: 
                if len(ans) < depth: ans.append(node.right.val)
                dfs(node.right, depth+1)
            if node.left: 
                if len(ans) < depth: ans.append(node.left.val)
                dfs(node.left, depth+1)
        dfs(root,2)
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
x = insertLevelOrder([1,2,3,None,5,None,None],0)
# y = insertLevelOrder([4,1,2],0)

sol =Solution()
print(sol.rightSideView(x))