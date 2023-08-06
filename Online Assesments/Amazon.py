def predictDays(day, k):
    # Write your code here
    ans = []
    candidates = set()
    days = 0
    for i in range(1, len(day)):
        if day[i] <= day[i-1]:
            days += 1
            if days >= k:
                candidates.add(i)
        else:
            days = 0
    days = 0
    for i in range(len(day)-2, -1, -1):
        if day[i] <= day[i+1]:
            days += 1
            if days >= k and i in candidates:
                ans.append(i+1)
        else:
            days = 0
    ans.reverse()
    return ans

print(predictDays([3,2,2,2,3,4],2))