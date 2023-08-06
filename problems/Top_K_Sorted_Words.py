from heapq import heappop, heappush


class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        heap = []
        dic = {}
        ans = [""]*k
        for word in words:
            if word in dic:
                dic[word] += 1
            else:
                dic[word] = 1
        for key in dic:
            heappush(heap, (-dic[key], key))
        
        for i in range(k):
            freq, word = heappop(heap)
            ans[i] = word
        return ans

sol = Solution()
print(sol.topKFrequent( ["the","day","is","sunny","the","the","the","sunny","is","is"] , 4))
