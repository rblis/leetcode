class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        start,end = newInterval
        ans = []
        for i,intv in enumerate(intervals):
            ss,ee = intv
            if end < ss: #interval finishes in between the next interval
                ans.append([start,end])
                return ans + intervals[i:]
            elif start > ee: #interval comes after the end of the current interval
                ans.append(intv)
            else: # a range covered by the interval
                start = min(start,ss)
                end = max(end, ee)
        ans.append([start,end])
        return ans


print(Solution().insert([[1,2],[3,5],[6,7],[8,10],[12,16]] , [4,8] ))