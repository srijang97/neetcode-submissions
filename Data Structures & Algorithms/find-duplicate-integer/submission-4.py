class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        sorted_nums = sorted(nums)
        prev = None

        for i, n in enumerate(sorted_nums):

            if n == prev:
                return n

            prev = n