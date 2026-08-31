class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefixProd = [0]*len(nums)
        suffixProd = [0]*len(nums)

        prefixProd[0] = nums[0]
        suffixProd[-1] = nums[-1]

        for i in range(1, len(nums)):

            prefixProd[i]  = prefixProd[i-1]*nums[i]
            suffixProd[len(nums)-i-1] = suffixProd[len(nums)-i]*nums[len(nums)-i-1]

        output = [0]*len(nums)
        output[0] = suffixProd[1]
        output[-1] = prefixProd[-2]

        for i in range(1, len(nums)-1):
            output[i] = prefixProd[i-1]*suffixProd[i+1]

        return output