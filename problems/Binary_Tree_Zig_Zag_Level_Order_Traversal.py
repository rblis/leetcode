
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self) -> str:
        return str(self.val)
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> list[list[int]]:
        if not root: return []
        ans = [[root.val]]
        bfs = []
        if root.left: bfs.append(root.left)
        if root.right: bfs.append(root.right)
        zig = False
        while bfs:
            temp = []
            for i in range(len(bfs)):
                node = bfs[i]
                if node.left != None: temp.append(node.left)
                if node.right != None: temp.append(node.right)
            level = []
            if zig:
                for node in bfs:
                    level.append(node.val)
            else:
                for i in range(len(bfs)-1,-1,-1):
                    node = bfs[i]
                    level.append(node.val)
            ans.append(level)
            zig = not zig
            bfs = temp
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
x = insertLevelOrder([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],0)
#x = insertLevelOrder([3,9,20,None,None,15,7],0)
print(Solution().zigzagLevelOrder(x))