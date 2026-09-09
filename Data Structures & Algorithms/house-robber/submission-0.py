class Solution:
    def rob(self, nums: List[int]) -> int:

        def dfs(i, winnings, cache):

            # if i >= len(nums):
            #     return 0

            if (i, winnings) in cache:
                return cache[(i, winnings)]
            
            withWinnings = winnings + nums[i]
            withoutWinnings = winnings

            if i + 2 < len(nums):
                withWinnings = dfs(i+2, winnings + nums[i], cache)
            
            if i + 1 < len(nums):
                withoutWinnings = dfs(i+1, winnings, cache) 

            cache[(i, winnings)] =  max(withWinnings, withoutWinnings)
            return cache[(i, winnings)]

        cache = {}
        return dfs(0, 0, cache)