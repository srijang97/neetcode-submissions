class Solution:
    def rob(self, nums: List[int]) -> int:

        def dfs(i, winnings, cache):

            if i >= len(nums):
                return 0

            if i in cache:
                return cache[i]
            
            withWinnings = dfs(i+2,winnings, cache)
            withoutWinnings = dfs(i+1, winnings, cache) 

            cache[i] =  max(nums[i] + withWinnings, withoutWinnings)
            return cache[i]

        cache = {}
        return dfs(0, 0, cache)