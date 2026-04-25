class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        max_len = 0
        for i in range(len(nums)):
            if nums[i] - 1 not in hashset:
                j = 1
                while nums[i] + j in hashset:
                    j+=1
                max_len = max(j,max_len)
        return max_len
