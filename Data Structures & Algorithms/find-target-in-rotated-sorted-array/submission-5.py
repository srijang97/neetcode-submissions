class Solution:
    def binarySearchMin(self, nums):

        L, R = 0, len(nums) - 1

        while L < R:

            mid = (L + R) // 2

            if nums[mid] > nums[R]:
                L = mid + 1
            else:
                R = mid

        return L

    def binarySearchTarget(self, nums, L, R, target):
        
        l = L
        r = R
        while l <= r:

            mid = (l + r) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        
        return -1

    def search(self, nums: List[int], target: int) -> int:
        minIdx = self.binarySearchMin(nums)
        print(minIdx)
        rightSearch = self.binarySearchTarget(nums, minIdx, len(nums)-1, target)
        leftSearch = self.binarySearchTarget(nums, 0, minIdx-1, target)

        if rightSearch != -1:
            return rightSearch

        if leftSearch != -1:
            return leftSearch

        return -1

            