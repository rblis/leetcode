class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        def bs(row):
            lo,hi = 0,len(matrix[row])-1
            while lo <= hi:
                mid = lo + hi >> 1
                if matrix[row][mid] < target:
                    lo = mid + 1 
                elif matrix[row][mid] > target:
                    hi = mid -1 
                else:
                    return mid
            return -1
        for i in range(len(matrix)):
            if bs(i) != -1:
                return True
        return False