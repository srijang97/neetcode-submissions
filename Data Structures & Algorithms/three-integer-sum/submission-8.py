class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums = sorted(nums)

        results = []

        for idx, n in enumerate(nums):
            
            if n > 0:
                break

            if idx > 0 and nums[idx] == nums[idx-1]:
                continue

            target = 0 - n
            
            i, j = idx + 1, len(nums) - 1
            while i < j:

                if nums[i] + nums[j] == target:
                    results.append([n, nums[i], nums[j]])
                    i += 1
                    j -= 1

                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
                
                elif nums[i] + nums[j] < target:
                    i += 1
                
                else:
                    j -= 1
        
        return results

