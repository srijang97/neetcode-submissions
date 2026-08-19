class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
      

        num_set = set(nums)

        max_length = 0

        length = 0

        for num in nums:

            if num-1 in num_set:
                length = 0
                continue
            else:
                length += 1
                num_to_check = num+1    
                while True:
                    if num_to_check in num_set:
                        length += 1
                        num_to_check += 1
                    else:
                        max_length = max(length, max_length)
                        length = 0
                        break

        max_length = max(length, max_length)

        return max_length



