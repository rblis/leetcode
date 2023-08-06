# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self) -> str:
        return str(self.val) + ' -> ' + (str(self.next.val) if self.next else 'X')
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fake = ListNode()
        fake.next = head
        def recurse(node: ListNode):
            if node:
                depth = recurse(node.next)
                if depth == n+1:
                    node.next = node.next.next
                return depth + 1
            else:
                return 1
        recurse(fake)
        return fake.next


vals = [1,2]
head = ListNode()
temp = head

for i, val in enumerate(vals):
    temp.val = val
    if i < len(vals)-1:
        temp.next = ListNode()
        temp = temp.next

Solution().removeNthFromEnd(head,2)




























# n = 1
# head = ListNode()
# temp = head
# for k in [1]:
#     temp.val = k
#     if k!=1:
#         temp.next = ListNode()
#         temp = head.next
# rev = []
# temp = head
# size = 0
# while temp != None:
#     rev.append(temp)
#     temp =temp.next
#     size += 1
# if size >= 3:
#     if n == 1:
#         rev[len(rev)-2].next = None
#     elif n == size:
#         head = head.next
#     else:
#         before = rev[len(rev)-n-1]
#         after = rev[len(rev)-n+1]
#         before.next = after
# elif size == 2:
#     if n == 1:
#         head.next = None
#     else:
#         head = head.next
# else:
#     head = None        
# print(head.val)
