'''
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
'''

from collections import deque


class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda x : x[0])
        intervals = deque(intervals)
        start,end = intervals[0][0], intervals[0][1]
        for i in range(len(intervals)):
            val = intervals.popleft()
            if val[0] <= end:
                end = max(end,val[1])
            else:
                intervals.append([start,end])
                start = val[0]
                end = val[1]
        intervals.append([start,end])
        return list(intervals)




print(Solution().merge([[1,3],[0,3],[2,3],[4,6],[4,5],[5,5],[0,2],[3,3]]
))