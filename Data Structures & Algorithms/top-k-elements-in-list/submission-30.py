class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = Counter(nums)

        buckets = [[] for i in range(1, len(nums)+1)]

        for n in freq:

            buckets[freq[n]-1].append(n)

        res = []
        needed = k

        for b in range(len(nums)-1, -1, -1):
            
            for num in buckets[b]:
                res.append(num)
                needed -= 1

                if needed == 0:
                    return res
        

