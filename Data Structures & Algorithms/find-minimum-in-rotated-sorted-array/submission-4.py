class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        L, R = 0, len(nums) - 1

        ans = float("inf")

        while L <= R:

            mid = (L + R) // 2

            if nums[L] < nums[R]:
                ans = min(ans, nums[mid])
                R = mid - 1
            elif nums[L] >= nums[R]:
                if nums[mid] > nums[R]:
                    L = mid + 1
                elif nums[mid] <= nums[R]:
                    ans = min(ans, nums[mid])
                    R = mid - 1                    
        return ans