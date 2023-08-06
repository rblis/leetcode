class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        ans = 0
        mono = []
        for i in range(len(heights)):
            x = heights[i]
            start = i
            while mono and mono[-1][0] > x:
                pop = mono.pop()
                ans = max(pop[0]*(i-pop[1]), ans)
                start = pop[1]
            mono.append((x,start))

        for h,i in mono:
            ans = max(ans, h*(len(heights) - i))
        return ans

print(Solution().largestRectangleArea( [2,1,5,6,2,3] ))