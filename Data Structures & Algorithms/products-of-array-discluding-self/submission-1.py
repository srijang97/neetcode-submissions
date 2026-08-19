class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix_product = [0]*len(nums)
        suffix_product = [0]*len(nums)

        prefix_product[0] = nums[0]
        suffix_product[-1] = nums[-1]

        for i in range(1, len(nums)):
            prefix_product[i] = nums[i] * (prefix_product[i-1])

        for j in range(1, len(nums)):
            suffix_product[len(nums)-1-j] = nums[len(nums)-1-j] * (suffix_product[len(nums)-j])

        output = [0]*len(nums)
        output[0] = suffix_product[1]
        output[-1] = prefix_product[-2]

        for i in range(1, len(nums)-1):

            output[i] = (prefix_product[i-1] )*(suffix_product[i+1])

        return output

        

        