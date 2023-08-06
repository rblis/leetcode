class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        dp = [False]*(len(s)+1)
        dp[len(s)] = True
        for i in range(len(s)-1, -1,-1):
            for word in wordDict:
                if (i+len(word)) <= len(s) and s[i:i+len(word)] == word:
                    #first part checks if the index that is iterating backwards can fit the dic word
                    #second part checks if a string slice starting from that index matches a dic word
                    dp[i] = dp[i + len(word)]
                if dp[i]: break
        return dp[0]


        