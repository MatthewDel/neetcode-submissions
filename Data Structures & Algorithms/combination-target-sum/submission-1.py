class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        sol = []
        def helper(nums, arr, target, index):
            nonlocal sol
            if target == 0:
                sol.append(arr[::])
                return
            elif target < 0:
                return 
            for i in range(index, len(nums)):
                arr.append(nums[i])
                helper(nums, arr, target -  nums[i], i)
                arr.pop()
        helper(nums, [], target, 0)
        return sol 
            