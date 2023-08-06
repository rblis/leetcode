"""
# Definition for a Node.
"""
from collections import deque


class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Node) -> Node:
        dup = Node(node.val)
        dic = {node.val: dup}
        que = deque([node])
        while que:#create clones
            og_node = que.popleft()
            for neib in og_node.neighbors:
                if neib.val not in dic:
                    dic[neib.val] = Node(neib.val)
                    que.append(neib)
        que.append(node)
        visited = set()
        while que:#assign clones as neighbors
            og_node = que.popleft()
            if og_node.val in visited: continue
            visited.add(og_node.val)
            for neib in og_node.neighbors:
                dic[og_node.val].neighbors.append(dic[neib.val])
                que.append(neib)



        return dup

