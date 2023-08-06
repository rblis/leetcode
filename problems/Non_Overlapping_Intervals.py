class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x : (x[0], x[1]) )
        last = intervals[0][1]
        count = 0
        for i in range(1,len(intervals)):
            aa,bb = intervals[i]
            if last > aa:#if last end value is greater than the starting val of next interval
                count += 1
                if last > bb: #we need to pick a end value that ends the earliest
                    last = bb
            else: #non overlapping
                last = bb #update the last value to be the next intervals last value
        return count

print(Solution().eraseOverlapIntervals(  [[-52,31],[-73,-26],[82,97],[-65,-11],[-62,-49],[95,99],[58,95],[-31,49],[66,98],[-63,2],[30,47],[-40,-26]] ))