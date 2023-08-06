# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#goal it to use the mid point of the linkedlist as the sub-root of the tree
#split the list in two recursively 
class Solution:
    def sortedListToBST(self, head:ListNode) -> TreeNode:
        def pickMid(node: ListNode):
            if not node:
                return 
            if not node.next:
                return TreeNode(node.val)
            premid, mid, tail = None, node, node
            while tail and tail.next:
                premid, mid, tail = mid, mid.next, tail.next.next
            premid.next = None
            root = TreeNode(mid.val)
            root.left = pickMid(node)
            root.right = pickMid(mid.next)
            return root
        return pickMid(head)