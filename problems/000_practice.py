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