'''
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
'''
from turtle import left


class Solution:
    def maxArea(self, height: list[int]) -> int:
        lo, hi = 0,len(height)-1
        ans = 0
        while lo < hi:
            ans = max(ans, min(height[lo], height[hi])*(hi-lo))
            if height[lo] < height[hi]:
                lo += 1
            else:
                hi -= 1
        return ans


sol = Solution()
print(sol.maxArea([1,8,6,2,5,4,8,3,7]))
































        # sz = len(height)
        # lo, hi = 0, sz-1
        # ans = 0
        # while lo < hi:
        #     ans = max(min(height[lo], height[hi])*(hi-lo), ans)
        #     if height[lo] < height[hi]:
        #         lo += 1
        #     else:
        #         hi -= 1
        # return ans

# sol= Solution()
# print(sol.maxArea([1,1]))

'''
        left, right = [0]*sz, [0]*sz
        ans = [0]*sz
        right[-1] = height[-1]
        left[0] = height[0]
        for i in range(1,sz):
            left[i] = max(height[i], left[i-1])
            right[-1-i] = max(height[-1-i], right[-i])
        
        for i in range(sz):
            ans[i] = min(left[i], right[i])
        
        
        print(left,right)
        return ans
'''