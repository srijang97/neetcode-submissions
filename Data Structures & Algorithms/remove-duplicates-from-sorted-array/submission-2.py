class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        if not nums:
            return 0

        place_to_write = 1

        for i in range(1, len(nums)):

            if nums[i] != nums[place_to_write-1]:
                nums[i], nums[place_to_write] = nums[place_to_write], nums[i]
                place_to_write += 1

        return place_to_write
