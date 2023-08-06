'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.
'''
class Solution:
    def trap(self, height: list[int]) -> int:
        if len(height) < 2:
            return 0
        left,right = [height[0]]*len(height), [height[-1]]*len(height)
        for i in range(1, len(height)):
            left[i] = max(height[i], left[i-1])
        for i in range(len(height)-2, 0, -1):
            right[i] = max(height[i], right[i+1])
        total  = 0
        for i in range(len(height)):
            val = min(right[i], left[i])-height[i]
            if val > 0:
                total += val
        return total

print(Solution().trap([4,2,3]))






























        # size, ans = len(height), 0
        # if size < 2:
        #     return 0
        # left,right= [0]*size, [0]*size

        # for i in range(1, size-1):
        #     left[i] = max(height[i-1], left[i-1])
        #     right[size-1-i] = max(height[size-i], right[size-i])
        # left[-1] = left[-2]
        # right[0] = right[1]
        # for i in range(size):
        #     mini = min(left[i], right[i])
        #     ans += mini-height[i] if mini-height[i] > 0 else 0
        # return ans































# def trap(height) -> int:
#     if len(height) < 3:
#         return 0
#     pool = 0
#     index = 1
#     while index < len(height):
#         if height[index] < height[index-1]:
#             end_index, add_pool = find_end(height, index-1)
#             if end_index != -1:
#                 pool += add_pool
#                 index = end_index
#             else: 
#                 index += 1
#         else:
#             index += 1

#     return(pool)

# def find_end(height, start_index) -> int:
#     start_height = height[start_index]
#     end_index = -1
#     pool = 0
#     for index in range(start_index+1, len(height)):
#         pool += start_height-height[index]
#         if height[index] >= start_height:
#             end_index = index
#             pool -= start_height-height[index]
#             break
#         elif height[index] > height[index-1]:
#             end_index = index
#     return end_index, pool


# print(trap([4,2,3]))
            