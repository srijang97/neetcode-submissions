class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0
        
        heapq.heapify(nums)

        max_length = 0
        length = 1
        prev = heapq.heappop(nums)

        while len(nums) > 0:
            
            curr = heapq.heappop(nums)
            if curr - prev > 1:

                max_length = max(max_length, length)
                length = 1
                prev = curr
            
            elif curr - prev == 1:
                length += 1
                prev = curr

            elif curr == prev:
                continue

        max_length = max(length, max_length)
        return max_length



