class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums = sorted(nums)

        resultSet = set()

        for idx, n in enumerate(nums):

            target = 0 - n
            
            i, j = idx + 1, len(nums) - 1
            while i < j:

                if nums[i] + nums[j] == target:
                    resultSet.add(tuple(sorted([n, nums[i], nums[j]])))
                    i += 1
                    j -= 1
                
                elif nums[i] + nums[j] < target:
                    i += 1
                
                else:
                    j -= 1
        
        return [list(x) for x in resultSet]

