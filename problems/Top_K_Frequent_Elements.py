from heapq import heappop, heappush


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        dic = {}
        for num in nums:
            if num not in dic:
                dic[num] = 1
            else:
                dic[num] += 1
        pq = []
        for key in dic:
            heappush(pq, (-dic[key], key))
        ans = []
        for i in range(k):
            ans.append(heappop(pq)[1])
        return ans



sol = Solution()
print(sol.topKFrequent([1,1,1,2,2,3], 2))


'''
Linear Bucket Sort
        buckets = [[] for _ in range(len(nums)+1)]
        counts = collections.defaultdict(int)
        for num in nums:
            counts[num] += 1        
        for key in counts:
            buckets[counts[key]].append(key)
        ans = []
        for i in range(len(buckets)-1,-1,-1):
            if buckets[i]:
                while buckets[i] and k > 0:
                    ans.append(buckets[i].pop())
                    k -= 1
        return ans

'''