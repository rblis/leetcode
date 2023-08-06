class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        band = set(banned)
        dic = {}
        word = ""
        for letter in paragraph:
            if letter.isalpha():
                word += letter.lower()
            else:
                if word not in band and word != "":
                    if word not in dic:
                        dic[word] = 1
                    else:
                        dic[word] += 1
                word = ""
        if word != "":
            if word not in dic:
                dic[word] = 1
            else:
                dic[word] += 1
        freq, ans = 0, ""
        for word in dic:
            if dic[word] > freq:
                freq = dic[word]
                ans = word
        return ans

sol = Solution()
print(sol.mostCommonWord("abc abc? abcd the jeff!", ["abc","abcd","jeff"]))

"Bob. hIt, baLl"
["bob", "hit"]

