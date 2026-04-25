class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        count = 0
        for i in range(len(nums)):
            if (nums[i] - 1) in nums_set:
                continue 
            else:
                running_count = 1
                control_var = nums[i] + 1
                while control_var in nums_set:
                    running_count += 1
                    control_var += 1
            count = max(count, running_count)
        
        return count
