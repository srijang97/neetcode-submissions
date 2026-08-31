class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numSet = set(nums)

        i = 0
        j = 1
        
        res = 0

        for i in range(len(nums)):
            
            if nums[i]-1 in numSet:
                continue
            else:
                seq = 1
                curr = nums[i]
                while curr + 1 in numSet:
                    seq += 1
                    curr += 1
                
                res = max(res, seq)

        return res

                
                


