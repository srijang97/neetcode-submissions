class Solution:
    def sortColors(self, nums: List[int]) -> None:

        # Your code goes here
        
        nextZero = 0

        for i in range(len(nums)):

            if nums[i] == 0:
                nums[nextZero], nums[i] = nums[i], nums[nextZero]
                nextZero += 1

        
        nextOne = nextZero

        for i in range(nextOne, len(nums)):

            if nums[i] == 1:
                nums[nextOne], nums[i] = nums[i], nums[nextOne]
                nextOne += 1
