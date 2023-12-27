# Definition for a binary tree node.
90101663084

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#     def __repr__(self) -> str:
#         return str(self.val) + ' -> ' + (str(self.next.val) if self.next else 'X')
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#     def __repr__(self) -> str:
#         return str(self.val)
# class TrieNode:
#     def __init__(self) -> None:
#         self.end = False
#         self.links = {}


from collections import defaultdict, Counter, deque
import heapq
import math

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        pass
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        vals = list(zip(position, speed))
        vals.sort(key=lambda x : -x[0])
        tot = 0
        print(vals)
        lastime = (target-vals[0][0])/vals[0][1]
        for i in range(1,len(position)):
            time = (target-vals[i][0])/vals[i][1]
            print(lastime,time)
            if time <= lastime:
                vals[i] = (-1,-1)
                lastime = max(time, lastime)
            else:
                lastime = time
        for val in vals:
            if val != (-1,-1):
                tot += 1
        print(vals)
        return tot
    

print(Solution().carFleet(10, [0,4,2], [2,1,3]))