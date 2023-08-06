'''
we maintain a decreasing mopnotonic stack that also contains the index 
of the item. Then whenever we find an element that is greater than the 
last most element in the stack we iterate backwards, popping off all
smaller items and subtracting the indexes we get how many days until the 
next higher temperature day by calculating from smaller item's index to 
the larger item's index
'''

class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        ans = [0]*len(temperatures)
        mono = [(temperatures[0],0)]
        for i in range(len(temperatures)):
            while len(mono) and mono[-1][0] < temperatures[i]:
                num, j = mono.pop()
                ans[j] = i-j
            mono.append((temperatures[i], i))
        return ans

sol = Solution()
print(sol.dailyTemperatures([73,74,75,71,69,72,76,73]))
















 



#dailyTemperatures([34,34,47,47,34,34,34,47,34,47,47,47,34,34,34,47,47,34,47,47,34,34,34,34,47,34,34,47,34,34,34,47,47,47,47,47,47,34,34,34,47,34,34,47,34,47,47,47,34,47,47,34,47,34,47,47,34,47,47,34,34,47,47,47,34,34,47,47,47,34,34,47,34,34,34,47,47,34,34,47,47,47,47,47,34,34,34,47,47,34,47,34,47,34,34,47,34,47,47,47,47,47,47,34,34,34,47,34,47,34,47,34,34,34,34,47,34,34,34,34,34,34,34,47,34,34,47,47,34,47,47,47,47,47,47,47,34,34,47,34,47,34,47,34,34,34,47,34,34,47,34,47,47,34,47,47,47,47,34,34,34,34,47,47,34,34,34,47,34,34,47,34,34,47,34,34,34,34,47,34,34,34,47,34,34,47,47,34,47,47,34,34,34,34,34,34,47,47,34,47,34,47,34,47,47,47,34,47,34,34,34,34,34,47,47,47,47,47,47,34,47,34,47,34,34,34,47,47,47,34,47,47,34,47,47,47,34,47,47,34,47,47,34,47,34,34,47,47,34,34,34,34,47,34,34,47,47,34,47,47,34,34,34,34,47,47,34,34,47,47,34,47,34,47,34,47,47,47,47,34,34,47,47,34,34,34,47,34,47,47,47,34,47,47,34,34,34,34,34,47,47,34,47,47,34,34,47,34,47,47,34,47,47,47,47,47,47,47,34,34,34,34,47,47,34,47,34,47,47,34,47,47,34,34,34,47,47,47,34,47,34,47,47,47,34,34,34,34,34,34,34,47,34,34,34,34,47,47,34,34,47,34,47,47,34,47,34,34,47,47,47,47,47,47,34,34,47,34,34,47,34,47,47,47,47,47,34,34,34,47,47,34,47,34,34,47,47,47,34,34,47,47,47,34,34,47,47,34,34,47,47,47,47,34,34,34,47,34,34,47,47,34,34,34,47,34,34,47,34,34,34,34,47,34,47,34,47,47,47,34,34,47,47,47,47,47,34,47,34,34,34,34,34,47,47,34,34,47,47,34,34,47,34,47,34,47,34,47,47,47,47,47,47,47,47,47,34,47,47,47,34,47,47,34,34,47,34,47,34,34,47,47,47,47,34,47,34,34,34,47,47,47,34,34,47,47,34,34,34,34,47,47,34,47,34,34,47,47,34,47,34,47,34,47,34,34,47,34,47,34,47,34,47,47,47,47,47,34,34,47,47,34,34,34,47,34,34,34,34,34,47,47,47,34,47,47,47,47,47,47,47,47,34,34,34,34,47,34,47,34,47,47,47,34,34,34,34,47,34,47,34,47,34,47,34,34,34,47,34,47,34,34,47,34,34,47,34,34,47,47,47,34,47,47,47,34,34,34,34,34,34,34,47,34,34,47,34,47,34,47,34,34,34,34,47,47,47,47,34,47,34,34,34,47,34,47,47,47,34,34,47,34,47,47,34,47,34,34,34,47,34,34,34,47,34,34,34,34,34,34,47,47,47,47,34,47,47,34,47,34,47,34,47,34,47,34,34,47,34,47,34,47])
'''
Brute Force Attempt
    next_high = [0]*len(T)
    for index,temp in enumerate(T):
        count = 0
        high_temp = 0
        for next_temp in range(index+1, len(T)):
            count +=1
            if T[next_temp] > temp:
                high_temp = T[next_temp]
                break
        if high_temp != 0:
            next_high[index] = count


Second Attempt using deque but did not work because I kept popping elements

    next_high = [-1]*71
    answer = [0]*len(T)
    for index,temp in enumerate(T):
        if next_high[temp-30] == -1:
            next_high[temp-30] = deque()
        next_high[temp-30].append(index)
    for index, temp in enumerate(T):
        for high_index in range(temp+1-30, 71):
            if next_high[high_index] != -1:
                if len(next_high[high_index]) > 0 and next_high[high_index][0] > index:
                    answer[index] = next_high[high_index].popleft()-index
                    break



    return next_high



    import heapq

temperatures = [73,74,75,71,69,72,76,73]
temperatures = temperatures
heap = []
ans = [0]*len(temperatures)
heapq.heappush(heap, (temperatures[0], 0))
for i in range(1, len(temperatures)):
    heapq.heappush(heap, (temperatures[i], i))
    while True:
        temp = heapq.heappop(heap)
        if temp[0] < temperatures[i]:
            ans[temp[1]] = i-temp[1]
        else:
            heapq.heappush(heap, temp)
            break
print(ans)
#Monotonic Stack

'''