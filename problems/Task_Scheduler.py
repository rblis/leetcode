import heapq
class Solution:
    def leastInterval(self, tasks: [str], n: int) -> int:
        dic = {}
        for task in tasks:
            if task in dic:
                dic[task] += 1
            else:
                dic[task] = 1
        heap = [ (-value, key) for key, value in dic.items()]
        heapq.heapify(heap) #heapify uses the first value of the tuple to determine priority order
        count = 0
        ans = []
        
        while count < len(tasks):
            temp = []
            for k in range(n+1):
                if len(heap) == 0:
                    if count >= len(tasks):
                        break
                    else:
                        ans.append('__')
                else:
                    item = heapq.heappop(heap)
                    ans.append(item[1])
                    if item[0] +1 <0:
                        item = (item[0]+1, item[1])
                        temp.append(item)
                    count += 1
                
            
            for item in temp:
                heapq.heappush(heap, item)

        return len(ans)


sol = Solution()
print(sol.leastInterval(["A","A","A","B","B","B", "B","C"], 2))