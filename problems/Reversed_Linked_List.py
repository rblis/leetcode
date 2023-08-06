# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self) -> str:
        return str(self.val) + ' -> ' + (str(self.next.val) if self.next else 'X')
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        def recurse(node: ListNode, pre=None) -> ListNode:
            if not node: #once we get to the last element we send it up the recursion tree
                return pre 
            temp = node.next #save the curren node's next value
            node.next = pre #save the next node value
            return recurse(temp, node)#swapped positions sent down the tree
        
        return recurse(head)


vals = [1,2,3]
head = ListNode()
temp = head
for val in vals:
    temp.val = val
    temp.next = ListNode()
    temp = temp.next

sol = Solution()
ans = sol.reverseList(head)
res = []
while ans.next != None:
    res.append(ans.val)
    ans = ans.next
print(res)