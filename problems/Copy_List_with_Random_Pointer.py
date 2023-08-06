class Node:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random
    def __repr__(self) -> str:
        return str(self.val) + ' -> ' + (str(self.next.val) if self.next else 'X')
class Solution:
    def copyRandomList(self, head: Node) -> Node:
        if not head:
            return None
        nhead = Node(head.val)
        a = head
        b = nhead
        dic = {}
        
        while a:
            if a.random:
                dic[a.random] = None
            b.val = a.val
            if not a.next:
                break
            b.next = Node(0)
            a = a.next
            b = b.next
        b.val = a.val
        a = head
        b = nhead
        while a:
            if a in dic:
                dic[a] = b
            a = a.next
            b = b.next
        a = head
        b = nhead
        while a:
            if a.random:
                b.random = dic[a.random]
            a = a.next
            b = b.next
        return nhead

            



vals = [1,2,3,4,5,6]
head = Node()
temp = head

for i, val in enumerate(vals):
    temp.val = val
    if i < len(vals)-1:
        temp.next = Node()
        temp = temp.next

Solution().copyRandomList(head)