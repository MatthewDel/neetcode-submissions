class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        sol = []
        def helper(res, running_set):
            if len(res) == len(nums):
                sol.append(res[::])
            
            for num in nums:
                if num not in running_set:
                    res.append(num)
                    running_set.add(num)
                    helper(res, running_set)
                    running_set.remove(num)
                    res.pop()
            
            return
        
        helper([], set())
        return sol
