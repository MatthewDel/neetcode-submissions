class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        ttl_sum = sum(nums) 
        if ttl_sum % 2 != 0:
            return False
        memo = {}
        
        def helper(curr, index):
            nonlocal ttl_sum
            if (curr, index) in memo:
                return memo[(curr, index)]
            if curr == (ttl_sum // 2):
                return True 
            if index == len(nums):
                return False 
            if curr > (ttl_sum // 2):
                return False
            memo[(curr,index)] = helper(curr, index + 1) or helper(curr + nums[index], index + 1)
            return memo[(curr,index)]
        return helper(0, 0)