class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        ans = 0
        for i,c in enumerate(number):
            if c == digit:
                ans =  max(ans, int(number[:i] + number[i+1:]))
        return str(ans)