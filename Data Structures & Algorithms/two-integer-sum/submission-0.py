class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashMap = {}

        for i, n in enumerate(nums):

            remainder = target - n

            if remainder in hashMap:

                r_idx = hashMap[remainder]

                return [r_idx, i] if r_idx < i else [i, r_idx]

            hashMap[n] = i

        
        