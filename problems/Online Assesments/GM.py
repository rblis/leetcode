dp = {}
def calc(num):
    global dp 
    if num in dp:
        return dp[num]
    ans = 0
    start = 0
    for key in dp.keys():
        if key < num:
            start = max(key, start)
    ans = 0 if start == 0 else dp[start]
    for i in range(start + 1, num+1):
        if i % 5 == 0 or i % 7 == 0:
            continue
        ans += i
        if i not in dp: dp[i] = ans
    return ans
for line in sys.stdin:
    print(calc(int(line)))