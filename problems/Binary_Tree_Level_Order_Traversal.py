from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        ans = []
        if not root:
            return ans
        ans.append([root.val])
        def bfs(nodes):
            level = []
            breadth = []
            nonlocal ans
            for node in nodes:
                if node.left:
                    level.append(node.left.val)
                    breadth.append(node.left)
                if node.right: 
                    level.append(node.right.val)
                    breadth.append(node.right)
            if len(level): 
                ans.append(level)
                bfs(breadth)
        bfs([root])
        return ans
class Solution:#queue based solution
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        ans = []
        level = deque([root])
        next_level = deque()
        curr_ans = []
        while level:
            node = level.popleft()
            if node: 
                curr_ans.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            if len(level) == 0:
                if curr_ans: ans.append(curr_ans)
                curr_ans = []
                level = next_level
                next_level = deque()
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
x = insertLevelOrder([3,4,5,1,2,2,2,2,None, 3, 4],0)
# y = insertLevelOrder([4,1,2],0)

sol =Solution()
print(sol.levelOrder(x))