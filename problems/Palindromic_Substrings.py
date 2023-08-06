class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        dp = [[False]*len(s) for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True
            count += 1

        for row in range(len(s)-2,-1,-1):
            for col in range(row+1, len(s)):
                if s[row] == s[col]:
                    if col-row < 2 or dp[row+1][col-1]: 
                        dp[row][col] = True
                        count += 1
        return count


sol = Solution()
print(sol.countSubstrings('aaaaa'))

# sett = set()
# def countSubstrings(s: str) -> int:
#     back_index, front_index = 0,1
#     count = 0
#     while front_index <= len(s) and back_index < len(s):
#         if checkPalindrome(s, back_index, front_index):
#             count += 1
#         front_index += 1
#         if front_index > len(s) and back_index < len(s):
#             back_index +=1 
#             front_index = back_index+1
#     return count
        

# def checkPalindrome(s, back_index, front_index):
#     substr = s[back_index:front_index]
#     if substr in sett:
#         return True
#     for index in range(0,int(len(substr)/2)):
#         if substr[index] != substr[-(index+1)]:
#             return False
#     sett.add(substr)
#     return True

# print(countSubstrings('abc'))
