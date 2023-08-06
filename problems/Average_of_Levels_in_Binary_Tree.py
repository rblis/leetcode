# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> list[float]:
        
        level = [root]
        ans = []
        while level:
            cur = []
            for i in range(len(level)):
                if level[i].left: cur.append(level[i].left)
                if level[i].right: cur.append(level[i].right)
            avg = 0
            for node in level:
                avg+=node.val
            ans.append(avg/len(level))
            level = cur
        return ans
