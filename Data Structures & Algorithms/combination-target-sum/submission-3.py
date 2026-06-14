class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        sol = []

        def helper(arr, running_sum, index):
            if (index >= len(nums) or running_sum > target):
                return
            
            if running_sum == target:
                sol.append(arr[::])
                return 
            
            for i in range(0, len(nums) - index):
                arr.append(nums[index + i])
                helper(arr, running_sum + nums[index + i], index + i)
                arr.pop()
            
            return
        
        helper([], 0, 0)
        return sol