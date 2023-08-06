# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self) -> str:
        return str(self.val) + ' -> ' + (str(self.next.val) if self.next else 'X')
class Solution:
    def mergeKLists(self, lists: list[ListNode]) -> ListNode:
        def mergeTwo(a: ListNode,b: ListNode):
            temp = ListNode()
            head = temp
            while a and b:
                if a.val < b.val:
                    temp.next = a
                    a = a.next
                else:
                    temp.next = b
                    b = b.next
                temp = temp.next
            if a:
                temp.next = a
            if b:
                temp.next = b
            return head.next
        if not len(lists):
            return None
        while len(lists) > 1:
            merged = []
            for i in range(0,len(lists), 2):
                a = lists[i]
                b = lists[i+1] if i+1 < len(lists) else None
                merged.append(mergeTwo(a,b))
            lists = merged
        return lists[0]


def mergeTwo(a: ListNode,b: ListNode):
    temp = ListNode()
    head = temp
    while a and b:
        if a.val < b.val:
            temp.next = a
            a = a.next
        else:
            temp.next = b
            b = b.next
    if a:
        temp.next = a
    if b:
        temp.next = b
    return head.next




a = [1,2,3]
b = [4,5]
aa = ListNode()
temp = aa

for i, val in enumerate(a):
    temp.val = val
    if i < len(a)-1:
        temp.next = ListNode()
        temp = temp.next
bb = ListNode()
temp = bb

for i, val in enumerate(b):
    temp.val = val
    if i < len(b)-1:
        temp.next = ListNode()
        temp = temp.next
mergeTwo(aa,bb)

# class Solution:
#     def mergeKLists(self, lists: list[ListNode]) -> ListNode:
#         ans = ListNode()
#         head = ans
#         while True:
#             pick = None
#             val = float('inf')
#             index= i = 0
#             for node in lists:
#                 if node:
#                     if node.val < val:
#                         val = node.val
#                         pick = node
#                         index = i
#                 i += 1
#             if pick:
#                 head.next = pick
#                 head = head.next
#                 lists[index] = lists[index].next
#             else:
#                 break
#         return ans.next