class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        cars = sorted(zip(position, speed), key=lambda x: -x[0])
        last = (target-cars[0][0])/cars[0][1]
        ans = 1
        for i in range(len(cars)):
            car = cars[i]
            time = (target-car[0])/car[1]
            if time > last:
                ans += 1
                last = time
        return ans
                

print(Solution().carFleet(12, [10,8,0,5,3], [2,4,1,1,3]))































#         vals = sorted(zip(position, speed), reverse=True)
#         ans, last = 0,0
#         for pos, spd in vals:
#             time = (target-pos)/spd
#             if time > last:
#                 ans += 1
#                 last = time
#         return ans
# sol = Solution()
# print(sol.carFleet(12, [3], [3]))