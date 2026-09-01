import heapq
class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        
        if not self.small or num <= -self.small[0]:
            heapq.heappush(self.small, -num)
        else:
            heapq.heappush(self.large, num)

        if len(self.small) > len(self.large)+ 1:
            popped = heapq.heappop(self.small)
            heapq.heappush(self.large, -popped)
        elif len(self.large) > len(self.small):
            popped = heapq.heappop(self.large)
            heapq.heappush(self.small, -popped)

    def findMedian(self) -> float:

        if len(self.small) > len(self.large):
            return -self.small[0]
        return (-self.small[0]+self.large[0])/2
        
        