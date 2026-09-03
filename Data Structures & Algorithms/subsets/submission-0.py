class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        result = [] 

        def dfs(idx, subset):
            nonlocal result
            if idx == len(nums):
                result.append(subset)
                return

            dfs(idx + 1, subset + [nums[idx]])
            dfs(idx + 1, subset)

            return

        dfs(0, [])
        return result