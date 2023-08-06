import collections
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        dic = collections.defaultdict(list)
        for word in strs:
            anagram = ''.join(sorted(word))
            dic[anagram].append(word)
        return dic.values()

sol = Solution()
print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))