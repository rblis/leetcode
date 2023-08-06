class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        tank = 0
        start = 0
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            # as long as there is gas in the tank we can keep moving
            if tank < 0: 
                tank = 0
                start = i+1
        return start
#if at any point, tank runs out of gas, we set our starting pt to the next index, since there
#  is guranteed to be a unique solution, we don't need to consider the gas stations between the 
# start and end (the station where tank runs out), because they are at best as good as the first
# gas station. So thats why we only need to consider the lgas stations that come after
# This way we inevitably end up at a gas station from where we can complete the entire circle

print(Solution().canCompleteCircuit( [2,3,4],
[3,4,3]
))

