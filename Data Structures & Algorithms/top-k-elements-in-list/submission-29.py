import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = Counter(nums)

        heap = []

        for n, v in freq.items():
            heapq.heappush_max(heap, (v, n))

        res = []

        for i in range(k):
            res.append(heapq.heappop_max(heap))

        return [x[1] for x in res]