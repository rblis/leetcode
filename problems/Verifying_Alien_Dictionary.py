class Solution:
    def isAlienSorted(self, words: list[str], order: str) -> bool:
        dic = {}
        for i in range(len(order)):
            dic[order[i]] = i
        for i in range(1,len(words)):
            a = words[i-1]
            b = words[i]
            for j in range(len(a)):
                if j > len(b): return False
                if a[j] != b[j]:
                    if dic[a[j]] > dic[b[j]]:
                        return False
                    else:
                        break
        return True

print(Solution().isAlienSorted(["hello","leetcode"]
,"hlabcdefgijkmnopqrstuvwxyz"
))