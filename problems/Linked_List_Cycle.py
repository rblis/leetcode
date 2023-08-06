# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        while head:
            if head.next == head:
                return True
            temp = head
            head = head.next
            temp.next = temp
        return False