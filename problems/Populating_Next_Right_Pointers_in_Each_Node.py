
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Node) -> Node:
        def dfs(node: Node, right: Node):
            if not node: return
            dfs(node.left, node.right)
            if right:
                node.next = right
                dfs(node.right, right.left)
            else:
                dfs(node.right, None)        
        dfs(root, None)
        return root