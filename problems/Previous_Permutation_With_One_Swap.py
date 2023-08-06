class Solution:
    def prevPermOpt1(self, arr: list[int]) -> list[int]:
        index = -1
        for i in range(len(arr)-2,-1,-1):
            if arr[i] > arr[i+1]:
                index = i
                break
        if index >= 0:
            right = index + 1
            for i in range(right + 1, len(arr)):
                #the index we are looking for has to be smaller than the target and has to be smallest if there are duplicates in a row
                if (arr[i] < arr[index] and arr[i] > arr[right]):
                    right = i

            arr[right],arr[index] = arr[index], arr[right]
                    
        return arr

print(Solution().prevPermOpt1([3,1,1,3]))
