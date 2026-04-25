class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (right + left) // 2
            value = nums[mid]

            if target > value:
                left = mid + 1
            elif target < value:
                right = mid - 1 
            else:
                return mid
        
        return -1