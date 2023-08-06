# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        head = ListNode()
        temp = head
        while True:
            if list1 == None:
                while list2 != None:
                    temp.next = list2
                    temp = temp.next
                    list2 = list2.next
                break
            elif list2 == None:
                while list1 != None:
                    temp.next = list1
                    temp = temp.next
                    list1 = list1.next
                break
            if list1.val < list2.val:
                temp.next = list1
                temp = temp.next
                list1 = list1.next
            else:
                temp.next = list2
                temp = temp.next
                list2 = list2.next
        return head.next
        