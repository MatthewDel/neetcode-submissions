class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        sol = [[]]
        def helper(nums, arr, index):
            nonlocal sol
            if index == len(nums):
                return 
            
            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i-1]:
                    continue 
                arr.append(nums[i])
                sol.append(arr[::])
                helper(nums, arr, i + 1)
                arr.pop()
        helper(nums, [], 0)
        return sol 