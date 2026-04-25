class Solution(object):
    def search(self, nums, target):
        left = 0
        right = len(nums)-1 
        while left <= right:
            mid = (left + right) // 2 
            if nums[mid] == target:
                return mid 
            elif nums[mid] >= nums[left]:
                if target > nums[mid]: 
                    left = mid + 1 
                elif target >= nums[left]:
                    right = mid - 1 
                else: #This implies that the target is not in the left interval
                    left = mid + 1
            elif nums[mid] <= nums[right]:
                if target >= nums[left]:
                    right = mid - 1
                elif target > mid:
                    left = mid + 1 
                elif target < mid:
                    right = mid - 1 
        return -1 