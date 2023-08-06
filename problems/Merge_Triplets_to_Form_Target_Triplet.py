class Solution:
    def mergeTriplets(self, triplets: list[list[int]], target: list[int]) -> bool:
        goal = []
        for triplet in triplets:
            if triplet[0] <= target[0] and triplet[1] <= target[1] and triplet[2] <= target[2]:
                if goal == []:
                    goal = triplet
                else:
                    goal =[max(goal[0],triplet[0]), max(goal[1],triplet[1]), max(goal[2],triplet[2])]
        return goal == target
        