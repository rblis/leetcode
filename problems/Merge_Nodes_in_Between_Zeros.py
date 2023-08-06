# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeNodes(self, head: ListNode) -> ListNode:
        node = head
        prev = None
        while node.next:
            if node.next.val != 0:
                node.val += node.next.val
                node.next = node.next.next
            else:
                prev = node
                node = node.next
        prev.next = None
        return head