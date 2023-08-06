# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self) -> str:
        return str(self.val) + ' -> ' + (str(self.next.val) if self.next else 'X')
class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head or not head.next:
            return
        slow = head
        fast = head
        prev = None
        temp = head
        while fast and fast.next: #when fast terminates, slow is at the middle of the list
            prev = slow #prev becomes the the end of the first half
            slow = slow.next #slow becomes the head of the second half
            fast = fast.next.next #fast moves at twice the speed of slow, becomes the tail of second half
        prev.next = None #this cuts the list in half
        #if list is odd then the second half has the extra odd node
        def reverse(node):
            prev = None
            curr = node
            while curr:
                nextnode = curr.next #save the reference to next node
                curr.next = prev #redirect the reference to the prev node
                prev = curr #set the prev node to the curr nodde to move along the list
                curr = nextnode #redirect the curr node to the next node

            return prev
        def merge(nodeA, nodeB):
            while nodeA:
                nextA = nodeA.next
                nextB = nodeB.next
                nodeA.next = nodeB
                if nextA:#enforces odd compability
                    nodeB.next = nextA
                nodeA = nextA
                nodeB = nextB
        fast = reverse(slow)
        merge(temp, fast)
'''
    def reorderList(self, head: ListNode) -> None:
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        def reverse(node: ListNode):
            back = None
            while node:
                temp = node.next
                node.next = back
                back = node
                node = temp
            return back
        
        mid = reverse(slow.next)
        slow.next = None
        def merge(a: ListNode,b: ListNode):
            while a and b:
                aa = a.next
                bb = b.next
                a.next = b
                b.next = aa
                a = aa
                b = bb
        merge(head, mid)
'''



vals = [1,2,3,4,5]
head = ListNode()
temp = head

for i, val in enumerate(vals):
    temp.val = val
    if i < len(vals)-1:
        temp.next = ListNode()
        temp = temp.next

sol = Solution()
sol.reorderList(head)
ans = head
while ans:
    print(ans.val)
    ans = ans.next
























#         """
#         Do not return anything, modify head in-place instead.
#         """
#         if not head.next or not head.next.next:
#             return
#         store = []
#         temp = head
#         while temp:
#             store.append(temp)
#             temp = temp.next
#         for i in range(len(store)>>1):
            
#             store[i].next = store[-1-i]
#             store[-1-i].next = store[i+1]
            
#         store[i+1].next = None
#         return head


# vals = [1,2,3,4,5]
# head = ListNode()
# temp = head
# for i, val in enumerate(vals):
#     temp.val = val
#     if i < len(vals)-1:
#         temp.next = ListNode()
#         temp = temp.next

# sol = Solution()
# ans = sol.reorderList(head)
# while ans:
#     print(ans.val)
#     ans = ans.next
