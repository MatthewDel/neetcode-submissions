class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)

        max_length = 0

        for i in range(len(nums)):
            running_length = 1
            temp = nums[i]
            while temp + 1 in nums_set:
                temp += 1
                running_length += 1

            max_length = max(max_length, running_length)
        
        return max_length