class compare(str):
    def __lt__(x,y):
        return str(x) + str(y) > str(y) + str(x)
class Solution:
    def largestNumber(self, nums: list[int]) -> str:           
        nums.sort(key=compare)
        ans = ''
        for num in nums:
            ans+= str(num)
        return '0' if ans[0] == '0' else ans

print(Solution().largestNumber([3,30,34,5,9]))