class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sol = []

        def helper(index, running_list):
            nonlocal sol
            
            if index >= len(nums):
                sol.append(running_list[::])
                return
            
            running_list.append(nums[index])
            helper(index + 1, running_list)
            running_list.pop()

            helper(index + 1, running_list)
        
        helper(0, [])
        return sol

