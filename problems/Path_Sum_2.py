'''

Given the root of a binary tree and an integer targetSum, 
return all root-to-leaf paths where each path's sum equals targetSum.

A leaf is a node with no children.
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
ans = []

def recur(node: TreeNode, sum, path, currentsum): 
    global ans
    if node == None:
        return
    if node.left == None and node.right == None:
        if currentsum + node.val == sum:
            path.append(node.val)
            ans.append(path)
    else:
        path.append(node.val)
        recur(node.left, sum, path.copy(), currentsum + node.val)
        recur(node.right, sum, path.copy(), currentsum + node.val)
        


def solution(root: TreeNode, targetSum):
    global ans
    if root == None: 
        return []        
    elif root.val == targetSum and root.left == None and root.right == None:
        return [[root.val]]
    else:
        recur(root.left, targetSum, [root.val], root.val)
        recur(root.right, targetSum, [root.val], root.val)
        return ans
    
nod = TreeNode()
nod.val = 1
nod.left = TreeNode()
nod.left.val = -2
nod.right = TreeNode()
nod.right.val = 3

nod.left.left = TreeNode()
nod.left.left.val = 1
nod.left.right = TreeNode()
nod.left.right.val = 3
nod.left.left.left = TreeNode()
nod.left.left.left.val = -1
print(solution(nod, 2))