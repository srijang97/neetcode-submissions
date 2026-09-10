class Solution:
    def rob(self, nums: List[int]) -> int:
        
        prev1 = nums[0]
        if len(nums) == 1:
            return prev1
            
        prev2 = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            curr_house = max(prev1 + nums[i], prev2)
            prev1 = prev2
            prev2 = curr_house
        
        return prev2