class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        tot = len(nums1) + len(nums2)
        half = tot >> 1 #number of elements in the halfway point
        small,big = nums1, nums2
        if len(nums1) > len(nums2):
            big = nums1
            small = nums2
        left = 0
        right = len(small) -1 
        while True: #neeed to find the halfway point of a theoretical merged array
            mid = left + right >> 1 #this is the halfway point of the smaller array
            mib = half - mid - 2 #this is supposed to be the halfway point of bigger array

            left_small = small[mid] if mid >= 0 else float('-inf')
            right_small = small[mid+1] if (mid + 1) < len(small) else float('inf')
            left_big = big[mib] if mib >= 0 else float('-inf')
            right_big = big[mib+1] if (mib + 1) < len(big) else float('inf')
# We know that left_small is smaller than right_small and left_big is smaller than right_big
# We have to ensure that in our imaginary merged array that left_small is also smaller than
# right_big and left_big is smaller than right_small. Then it becoems the true midpoint of an
# merged array in terms of the midpoint of left and right partitions of that merged array
            if left_small <= right_big and left_big <= right_small:
                if tot % 2:
                    return min(right_small, right_big) # since the smaller value comes before the right value, in a sorted merged list the smaller value is the actual median
                # the right most 
                return (max(left_small, left_big) + min(right_small, right_big)) / 2

            elif left_small > right_big:
                right = mid - 1
            else:
                left= mid + 1


print(Solution().findMedianSortedArrays([1,2,3,4,5,6,7,8], [1,2,3,4,5]))