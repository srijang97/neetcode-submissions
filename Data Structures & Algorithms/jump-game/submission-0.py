class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        idxToReach = len(nums)-1

        for i in range(len(nums)-2, -1, -1):

            if nums[i] >= idxToReach - i:
                idxToReach = i

            else:
                continue

        return idxToReach == 0