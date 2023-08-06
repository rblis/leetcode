class Solution:
    def minimumCardPickup(self, cards: list[int]) -> int:
        dups = {}
        ans = float('inf')
        for i,card in enumerate(cards):
            if card not in dups:
                dups[card] = i
            else:
                ans = min(i-dups[card] + 1, ans)
                dups[card] = i
        return ans if ans != float('inf') else -1