from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        num_counter = Counter(nums)
        sorted_counts = sorted(list(num_counter.values()))[-k:]

        ans = set()

        for n in nums:

            if num_counter[n] in sorted_counts:
                ans.add(n)
            
        return list(ans)

