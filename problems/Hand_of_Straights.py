import collections


class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        if len(hand)%groupSize != 0: return False
        hand.sort()
        dic = collections.defaultdict(int)
        for i in hand:
            dic[i] += 1
        i,count, restart = 0, 0, -1
        last = hand[0]
        group = set()
        while i < len(hand):
            if hand[i] not in group and dic[hand[i]] > 0:
                if last != -1 and hand[i] - last > 1: return False
                group.add(hand[i])
                dic[hand[i]] -= 1
                count += 1
                last= hand[i]
            elif hand[i] in group and dic[hand[i]] > 0 and restart == -1:
                restart = i
            if count == groupSize:
                count = 0
                group = set()
                last = -1
                if restart != -1:
                    i = restart-1
                    restart = -1
            i+= 1
        
        return True if count == 0 else False

print(Solution().isNStraightHand([1,1,2,2,3,3],3))