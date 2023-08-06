class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        ans = 0
        cet, seen = set(), set()
        for num in nums:
            cet.add(num)
        for num in cet:
            if num not in seen:
                seen.add(num)
                count  = 1
                cur = num
                while True:
                    if cur+1 in cet:
                        seen.add(cur+1)
                        cur += 1
                        count += 1
                    else:
                        ans = max(count, ans)
                        break
        return ans

sol = Solution()
print(sol.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
