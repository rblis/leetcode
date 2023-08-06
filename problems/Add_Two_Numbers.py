class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self) -> str:
        return str(self.val) + ' -> ' + (str(self.next.val) if self.next else 'X')
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans = ListNode()
        a,b,c = l1,l2, ans
        carry = 0
        while a or b or carry:
            vala = a.val if a else 0
            valb = b.val if b else 0
            val = vala + valb + carry
            carry = val//10
            c.val = val%10
            a = a.next if a else None
            b = b.next if b else None
            c.next = ListNode() if a or b or carry else None
            c = c.next
        
        return ans

a = [2,4,3]
b = [5,6,4]
aa = ListNode()
bb = ListNode()
temp = aa

for i, val in enumerate(a):
    temp.val = val
    if i < len(a)-1:
        temp.next = ListNode()
        temp = temp.next
temp = bb
for i, val in enumerate(b):
    temp.val = val
    if i < len(b)-1:
        temp.next = ListNode()
        temp = temp.next


Solution().addTwoNumbers(aa,bb)


































# l1 = ListNode(0)
# l2 = ListNode(0) 
# a1 = [9,9,9,9,9,9,9]
# a2 = [9,9,9,9]
# p = l1
# for i in range(len(a1)):
#     p.val = a1[i]
#     if i != len(a1)-1:
#         p.next = ListNode()
#         p = p.next
# p = l2
# for i in range(len(a2)):
#     p.val = a2[i]
#     if i != len(a2)-1:
#         p.next = ListNode()
#         p = p.next

# ss = []
# sums = ListNode()
# ans = sums
# sum = l1.val + l2.val
# carry = 0
# if sum >= 10:
#     carry = 1
# ans.val = sum % 10
# ss.append(ans.val)
# l1, l2 = l1.next, l2.next

# while l1 != None and l2 != None:
#     sums.next = ListNode()
#     sums = sums.next
#     sum = l1.val + l2.val + carry
#     if sum >= 10:
#         carry = 1
#     else:
#         carry = 0
#     sums.val = sum % 10  
#     ss.append(sum%10)  
#     l1, l2 = l1.next, l2.next


    
# if l1 == None and l2!=None:
#     sums.next = ListNode()
#     sums = sums.next
#     while l2 != None:
#         sum = l2.val + carry
#         if sum >= 10:
#             carry = 1
#         else:
#             carry = 0
#         sums.val = sum % 10
#         ss.append(sum %10)
#         if l2.next != None:
#             sums.next = ListNode()
#             sums = sums.next
#         l2 = l2.next
# elif l2 == None and l1 != None:
#     sums.next = ListNode()
#     sums = sums.next
#     while l1 != None:
#         sum = l1.val + carry
#         if sum >= 10:
#             carry = 1
#         else:
#             carry = 0
#         sums.val = sum % 10
#         ss.append(sum % 10)
#         if l1.next != None:
#             sums.next = ListNode()
#             sums = sums.next
#         l1 = l1.next
# if carry:
#     sums.next = ListNode()
#     sums = sums.next
#     sums.val = carry
#     ss.append(carry)
        # result = ListNode(0)
        # result_tail = result
        # carry = 0
                
        # while l1 or l2 or carry:            
        #     val1  = (l1.val if l1 else 0)
        #     val2  = (l2.val if l2 else 0)
        #     carry, out = divmod(val1+val2 + carry, 10)    
                      
        #     result_tail.next = ListNode(out)
        #     result_tail = result_tail.next                      
            
        #     l1 = (l1.next if l1 else None)
        #     l2 = (l2.next if l2 else None)
               
        # return result.next