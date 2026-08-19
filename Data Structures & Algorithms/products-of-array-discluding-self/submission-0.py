class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix_product = [0]*len(nums)
        suffix_product = [0]*len(nums)

        for i in range(len(nums)):
            prefix_product[i] = nums[i] * (prefix_product[i-1] if i > 0 else 1)

        for j in range(len(nums)):
            suffix_product[len(nums)-1-j] = nums[len(nums)-1-j] * (suffix_product[len(nums)-j] if j > 0 else 1)

        output = [0]*len(nums)

        for i in range(len(nums)):

            output[i] = (prefix_product[i-1] if i > 0 else 1)*(suffix_product[i+1] if i < (len(nums) - 1) else 1)

        return output

        

        