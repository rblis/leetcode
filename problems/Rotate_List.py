# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self) -> str:
        return str(self.val) + ' -> ' + (str(self.next.val) if self.next else 'X')
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        sz= 0
        temp = head
        def recurse(node: ListNode):
            nonlocal sz, head
            if node:
                sz+=1
                depth = recurse(node.next)
                if depth == 1:
                    node.next = head
                if k%sz  == depth:
                    head = node
                if k%sz + 1 == depth:
                    node.next = None
                return depth + 1
            else:
                return 1
        recurse(temp)
        return head

vals = [1,2,3,4,5]
head = ListNode()
temp = head

for i, val in enumerate(vals):
    temp.val = val
    if i < len(vals)-1:
        temp.next = ListNode()
        temp = temp.next

Solution().rotateRight(head, 2)