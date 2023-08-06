class Solution:
    def bagOfTokensScore(self, tokens: list[int], power: int) -> int:
        score = 0
        tokens.sort()
        lo,hi = 0, len(tokens)-1
        while lo <= hi:
            if power >= tokens[lo]:
                power -= tokens[lo]
                score += 1
                lo += 1
            elif score >= 1 and power < tokens[lo] and lo < hi:
                power += tokens[hi]
                hi -= 1
                score -= 1
            else:
                hi -= 1
        return score

print(Solution().bagOfTokensScore(   tokens = [100,200], power = 150   ))
        