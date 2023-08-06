# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self) -> str:
        return str(self.val) + ' -> ' + (str(self.next.val) if self.next else 'X')

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        temp = head
        def reverse(node, prev):
            count = 0
            temp = node
            while count < k:
                next_node = node.next
                node.next = prev
                prev = node
                node = next_node
                count += 1
            return (prev,temp)
        size = 1
        while temp:
            temp = temp.next
            size += 1
        i = 0
        start = head
        new_head = None
        prev = None
        while i < size:
            end = start
            join = None
            j = 0
            while j < k:                
                end = end.next
                j +=1
            if not new_head:
                new_head,prev = reverse(start, None)
                start.next = end
            else:                
                join,temp = reverse(start, prev)
                prev.next = join
                prev = temp
                start.next = end
            start = start.next
            i += k
            if i + k >= size: break
        return new_head

def genlist(vals):
    head = ListNode()
    temp = head
    for i, val in enumerate(vals):
        temp.val = val
        if i < len(vals)-1:
            temp.next = ListNode()
            temp = temp.next
    return head
x = [1,2,3,4,5]
head = genlist(x)
Solution().reverseKGroup(head, 2)