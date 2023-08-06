# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        node = head
        prev = None
        new_head = None
        while node and node.next:
            temp = node.next
            node.next = node.next.next
            temp.next = node
            if not new_head:
                new_head = temp
            if prev:
                prev.next = temp
            prev = node
            node = node.next
        return new_head
        