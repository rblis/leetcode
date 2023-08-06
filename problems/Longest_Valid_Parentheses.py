s = ')()())'
ans, left, right, = 0, 0, 0
size = len(s)
for c in s:
    if c == '(':
        left += 1
    else:
        right += 1
    if left == right:
        ans =  max(ans, left+right)
    elif right > left:
        left = right = 0
left = right = 0
for i in range(size-1,-1, -1):
    if s[i] == '(':
        left += 1
    else:
        right +=1
    if left == right:
        ans = max(ans, left+right)
    elif left > right:
        left =right = 0

print(ans)


# dp = [0]*len(s)
# for i in range(len(s)):
#     if s[i] == ')':
#         right += 1
#     else:
#         left+= 1
#     dp[i] = (left, right)
# print(dp)
# start, adj = 0,0
# for i in range(len(s)):
#     if dp[i][0] == dp[i][1]:
#         start = dp[i]
#         adj = dp[i-1]


# while i < len(s):
#     if left >= right:
#         res += 1
#         if s[i] == '(':
#             left += 1
#         elif s[i] == ')':
#             right += 1
#     else:
#         if ans < res:
#             ans = res -1
#         res, left, right = 0, 0, 0
#         i-= 1
#     i+=1
# print(ans)