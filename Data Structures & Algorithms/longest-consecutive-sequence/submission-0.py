class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = set(nums)
        longest = 0
        for i in range(len(nums)):
            if nums[i]-1 not in hash_set:
                traverse = 1
                while nums[i] + traverse in hash_set:
                    traverse += 1
                longest = max(longest, traverse)
        return longest