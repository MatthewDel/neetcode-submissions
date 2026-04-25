class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hashmap = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        sol = []
        if not digits:
            return []
        def backtrack(index, temp):
            if index == len(digits):
                sol.append(''.join(temp))
                return
            for j in range(len(hashmap[digits[index]])):
                temp.append(hashmap[digits[index]][j])
                backtrack(index+1, temp)
                temp.pop()
        backtrack(0, [])
        return sol 