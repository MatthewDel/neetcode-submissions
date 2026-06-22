class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        sol = [[]]

        def helper(running_list, index):
            if index >= len(nums):
                return
            
            while index < len(nums):
                running_list.append(nums[index])
                sol.append(running_list[::])
                helper(running_list, index + 1)
                running_list.pop()

                index += 1 

                while index < len(nums) and nums[index] == nums[index - 1]:
                    index += 1 
            
        helper([], 0)
        return sol
