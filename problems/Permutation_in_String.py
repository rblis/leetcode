class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        dic = {}
        check = {}
        for c in s1:
            check[c] = check.get(c,0) + 1
        for i in range(len(s1)):
            dic[s2[i]] = dic.get(s2[i], 0) + 1
        if dic == check: return True
        end = 0
        for front in range(len(s1), len(s2)):
            dic[s2[front]] = dic.get(s2[front], 0) + 1
            dic[s2[end]] -= 1
            if dic[s2[end]] == 0: dic.pop(s2[end])
            end += 1
            if dic == check: return True
        return False

sol = Solution()
print(sol.checkInclusion("abcdxabcde", "zbcdeabcdxa"))
