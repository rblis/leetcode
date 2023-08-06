import collections


class TrieNode:
    def __init__(self) -> None:
        self.links = {}
        self.end = False


class Solution:
    def matchingSuffixPairs(self, words: list[str]) -> int:
        head = TrieNode()
        temp = head
        dic = collections.defaultdict(int)
        for i,word in enumerate(words):
            temp = head
            dic[word] += 1
            for i in range(len(word)-1,-1,-1):
                c = word[i]
                if c not in temp.links:
                    temp.links[c] = TrieNode()
                temp = temp.links[c]
            temp.end = True
        temp = head
        ans = 0
        for word in words:
            temp = head
            cur = ''
            for i in range(len(word)-1,-1,-1):
                c = word[i]
                cur = c + cur
                if c in temp.links:
                    temp = temp.links[c]
                else:
                    break
                if temp.end:
                    if cur == word:
                        ans += dic[cur] -1
                        if dic[cur] > 1: dic[cur] -= 1
                    else:
                        ans += dic[cur]        
        return ans 



words = ['a','ba','a','a']
#words = ['cba','ba','ca', 'a','a','b']
#words = ['back', 'comeback', 'backdoor', 'gammon','backgammon', 'come', 'door']
print(Solution().matchingSuffixPairs(words))