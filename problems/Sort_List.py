# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self) -> str:
        return str(self.val) + ' -> ' + (str(self.next.val) if self.next else 'X')
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        if not head.next:
            return head
        def merge(aa,bb):
            a,b = aa,bb
            node = ListNode()
            temp = node
            while a and b:
                if a.val > b.val:
                    temp.next = b
                    temp = temp.next
                    b = b.next
                else:
                    temp.next = a
                    temp = temp.next
                    a = a.next
            if a:
                temp.next = a
            if b: 
                temp.next = b
            return node.next

        def split(node):
            fast,slow, prev = node, node, None
            count = 0
            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next
                count += 2
            prev.next = None
            if count <= 2:
                if not slow.next:
                    return merge(node,slow)
                else:
                    temp = slow.next
                    slow.next = None
                    return merge(merge(slow, temp), node)
            else:
                return merge(split(node), split(slow))
        return split(head)


a = [-1,5,3,4,0] #[1,3,2,4]
b = [2,4]
c = [1,3]
def genlist(vals):
    head = ListNode()
    temp = head
    for i, val in enumerate(vals):
        temp.val = val
        if i < len(vals)-1:
            temp.next = ListNode()
            temp = temp.next
    return head

print(Solution().sortList(genlist(a)))