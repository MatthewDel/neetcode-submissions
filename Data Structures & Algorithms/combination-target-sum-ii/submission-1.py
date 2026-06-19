class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        sol = []
        candidates.sort()
        def helper(value, running_list, index):
            nonlocal sol

            if value == target:
                sol.append(running_list[::])
                return

            if index >= len(candidates) or value > target:
                return
            
            while index < len(candidates):
                running_list.append(candidates[index])
                helper(value + candidates[index], running_list, index + 1)
                running_list.pop()
                index += 1

                while index < len(candidates) and candidates[index] == candidates[index - 1]:
                    index += 1
            

                

                
            
            return
        
        helper(0, [], 0)
        return sol



    