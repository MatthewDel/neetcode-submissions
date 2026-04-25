class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        sol = []
        def helper(temp, running_set):
            if len(temp) == len(nums):
                sol.append(temp[::])
                return
            
            for i in range(len(nums)):
                if nums[i] in running_set:
                    continue 
                running_set.add(nums[i])
                temp.append(nums[i])
                helper(temp, running_set)
                temp.pop()
                running_set.remove(nums[i])
        
        helper([], set())
        return sol 
            