import heapq


class MedianFinder:

    def __init__(self):
        self.small, self.big = [],[]#max heap (negative numbers), min heap(normal nums)


    def addNum(self, num: int) -> None:
        sml, big = self.small, self.big
        heapq.heappush(sml, -num)#add to the small side first
        #if the biggest num from smallest is greater than smallest from the big side
        if sml and big and -sml[0] > big[0]:
            heapq.heappush(big, -heapq.heappop(sml))
        if len(big) > len(sml):#if big side is more than small
            heapq.heappush(sml, -heapq.heappop(big))
        if len(big) + 1 < len(sml): #if bigger side has fewer than small-1 elements
            heapq.heappush(big, -heapq.heappop(sml))
    
    def findMedian(self) -> float:
        if (len(self.small) + len(self.big))%2:
            return -self.small[0]
        else:
            return (-self.small[0] + self.big[0]) / 2

obj = MedianFinder()
obj.addNum(1)
print(obj.findMedian())
obj.addNum(2)
print(obj.findMedian())
obj.addNum(3)
print(obj.findMedian())
obj.addNum(4)
print(obj.findMedian())
obj.addNum(5)
print(obj.findMedian())