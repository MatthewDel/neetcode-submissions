class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        sol = []
        print(candidates)

        def helper(candidates, arr, target, index):
            if target == 0:
                sol.append(arr[::])
            elif target < 0:
                return 
            
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i - 1]:
                    continue 
                arr.append(candidates[i])
                helper(candidates, arr, target - candidates[i], i + 1)
                arr.pop()
                
    
        helper(candidates, [] , target , 0)
        return sol 