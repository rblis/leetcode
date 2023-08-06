from collections import defaultdict
class Solution:
    def maxRepOpt1(self, text: str) -> int:
        ans = 0
        lo = 0
        dic = defaultdict(int)
        for c in text:
            dic[c] += 1
        if len(dic) == 1: 
            return len(text)
        cur = defaultdict(int)
        for hi in range(len(text)):
            cur[text[hi]] += 1
            if len(cur) > 2:
                pass
            elif len(cur) == 2:
                pass