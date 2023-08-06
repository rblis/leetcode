class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        n = len(image)
        if n == 1:
            image[0][0] = 0 if image[0][0] else 1
            return image
        for row in range(n):
            for col in range(n//2):
                temp = image[row][col]
                image[row][col] = 0 if image[row][-col-1] else 1
                image[row][-col-1] = 0 if temp else 1
            if n%2==1: image[row][col+1] = 0 if image[row][col+1] else 1

        return image

print(Solution().flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]))
test = 1
print(test^1)