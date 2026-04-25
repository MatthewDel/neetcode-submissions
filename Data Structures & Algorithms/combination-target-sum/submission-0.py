class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        sol = []
        def helper(sum, index, group):
            if sum == target:
                sol.append(group[::])
            elif sum > target:
                return 
            for i in range(index, len(nums)):
                group.append(nums[i])
                helper(sum + nums[i], i, group)
                group.pop()
        helper(0,0,[])
        return sol 