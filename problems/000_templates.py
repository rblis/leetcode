class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self) -> str:
        return str(self.val) + ' -> ' + (str(self.next.val) if self.next else 'X')
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self) -> str:
        return str(self.val)


a = [1,2,3,4,5]
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


#print 2D list
matrix = [[0 for x in range(len(5))] for y in range(len(5))]
print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in matrix]))

def insertLevelOrder(arr, i):
    root = None
    # Base case for recursion 
    if i < len(arr):
        root = TreeNode(arr[i]) if arr[i] != None else None
        if root:
            # insert left child 
            root.left = insertLevelOrder(arr, 2 * i + 1)
            # insert right child 
            root.right = insertLevelOrder(arr, 2 * i + 2)
    return root
x = insertLevelOrder([3,9,20,None,None,15,7],0)