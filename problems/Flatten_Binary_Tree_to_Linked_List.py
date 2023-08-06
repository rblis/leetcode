# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self) -> str:
        return str(self.val)
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def flat(node):
            if not node: return None
            left_tail = flat(node.left)
            right_tail = flat(node.right)
            if left_tail:
                left_tail.right = node.right
                node.right = node.left
                node.left = None
            if right_tail:
                return right_tail
            elif left_tail:
                return left_tail
            else:
                return node
            
        flat(root)
        print(root)

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
x = insertLevelOrder([1,2,3],0)
Solution().flatten(x)