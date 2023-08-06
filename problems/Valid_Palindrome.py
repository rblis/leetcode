class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) <= 1:
            return True
        ss = ""
        for letter in s:
            if letter.isalnum():
                ss += letter.lower()
        if len(ss) <= 1:
            return True
        for i in range(len(ss)//2):
            a, b = ss[i] , ss[-1-i]
            if ss[i] != ss[-1-i]:
                return False
        return True

sol = Solution()
print(sol.isPalindrome("A man, a plan, a canal: Panama"))