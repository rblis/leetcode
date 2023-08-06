
class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[False] * len(s) for _ in range(len(s))]
        max_len = 1
        start_pos = 0
        for i in range(len(s)):
            dp[i][i] = True 
        for start in range(len(s)-2, -1,-1):
            for end in range(start+1, len(s)):                
                if s[start] == s[end]:
                    if end-start == 1 or dp[start+1][end-1] == True:
                        dp[start][end] = True
                        if end-start+1 > max_len:
                            max_len = end-start+1
                            start_pos = start                
        return s[start_pos:start_pos + max_len]

x = 'abdbaccabd'
print(Solution().longestPalindrome("cbbd"))


        #traversing diagonally is bad for cache latency
        # col = 2
        # while col<len(s):
        #     start, end = 0, col
        #     while end < len(s):
        #         deepee(start,end)
        #         start+=1
        #         end+=1   
        #     col += 1          






#         if len(s) == 1:
#             return s
#         if (len(s) == 2):
#             if s[0] == s[1]:
#                 return s
#             else:
#                 return s[0]
#         ansodd = ""
#         anseven = ""
#         szodd, szeven = 1, 0
#         even, odd = False, False
#         for i in range(len(s)):
#             for j in range(1, len(s)-i):              

#                 a, b, c = s[i-j], s[i-j + 1], s[i+j]
#                 sodd, seven = s[i-j:i+j+1], s[i-j+1:i+j+1]
#                 if even:
#                     pass
#                 elif s[i-j + 1] == s[i+j]:
#                     szeven += 2
#                     if i-j+1 <= 0 or i+j == len(s)-1:
#                         if szeven > len(anseven):
#                             anseven = s[i-j+1:i+j+1]
#                         szeven = 0
#                         even = True
#                 else:
#                     if szeven > len(anseven):
#                         anseven = s[i-j+2:i+j]
#                     szeven = 0
#                     even = True


#                 if odd:
#                     pass
#                 elif s[i+j] == s[i-j]:
#                     szodd += 2
#                     if i-j <= 0 or i+j == len(s)-1:
#                         if szodd > len(ansodd):
#                             ansodd = s[i-j:i+j+1]
#                         szodd = 1
#                         odd = True
#                 else:
#                     if szodd > len(ansodd):
#                         ansodd = s[i-j+1:i+j]
#                     szodd = 1
#                     odd = True


#                 if even and odd:
#                     even, odd = False, False
#                     break

#         return ansodd if len(ansodd) > len(anseven) else anseven

# sol = Solution()
# print(sol.longestPalindrome("abcbe"))
# print(sol.longestPalindrome("ccd"))
# print(sol.longestPalindrome("cbaaba"))


# s = 'aaaaa'
# ans = 0
# sol = s[0]
# size = len(s)
# if size == 1:
#     ans = 1
#     sol = s
# elif size == 2:
#     if s[0] == s[1]:
#         sol = s
#     else:
#         sol = s[0]
# for i in range(0,size):
#     if i-1 >= 0 and s[i] == s[i-1]:
#         j, palen = 1, 2
#         while i+j < size and i-j-1 >= 0 and s[i+j] == s[i-1-j]:
#             palen += 2 
#             j += 1
#         if palen > ans:
#             ans =  palen
#             sol = s[i-j:i+j]
#     if i+1 < size and i-1 >= 0 and s[i+1] == s[i-1]:
#         j, palen = 2, 3
#         while i+j < size and i-j >= 0 and s[i+j] == s[i-j]:
#             palen += 2 
#             j += 1
#         if palen > ans:
#             ans =  palen
#             sol = s[i-j+1:i+j]


# if size == 1:
#     ans = 1
#     sol = s
# elif size % 2 == 0: #even length
#     for i in range(1,size):
#         if s[i] == s[i-1]:
#             j, palen = 1, 2
#             while i+j < size and i-j-1 >= 0 and s[i+j] == s[i-1-j]:
#                 palen += 2 
#                 j += 1
#             if palen > ans:
#                 ans =  palen
#                 sol = s[i-j:i+j]
# else: #odd length
#     for i in range(1,size-1):
#         if s[i+1] == s[i-1]:
#             j, palen = 2, 3
#             while i+j < size and i-j-1 >= 0 and s[i+j] == s[i-j]:
#                 palen += 2 
#                 j += 1
#             if palen > ans:
#                 ans =  palen
#                 sol = s[i-j+1:i+j]
