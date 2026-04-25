class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        maxCount = 0
        for num in nums:
            if num - 1 in hashset:
                continue
            
            temp = num
            count = 1
            while temp + 1 in hashset:
                temp += 1
                count += 1
            maxCount = max(count, maxCount)
        return maxCount