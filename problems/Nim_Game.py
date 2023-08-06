class Solution:
    def canWinNim(self, n: int) -> bool:
        if n<=3: return True
        if n%2 == 0 and n%3 > 0: return False

print(Solution().canWinNim(8))