class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1 
        res = nums[0]
        while left <= right:
            mid = (left + right) // 2
            if nums[left] <= nums[right]:
                return min(res, nums[left])
            if nums[left] <= nums[mid]:
                left = mid + 1
            elif nums[right] >= nums[mid]: 
                res = min(res, nums[mid])
                right = mid - 1 
        return res