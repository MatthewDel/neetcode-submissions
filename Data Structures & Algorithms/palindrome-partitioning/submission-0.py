class Solution:
    def partition(self, s: str) -> List[List[str]]:
        sol = []

        def ispalindrome(string):
            left = 0
            right = len(string) - 1 
            while left < right:
                if string[left] != string[right]:
                    return False
                left += 1
                right -= 1
            return True 

        def helper(s, arr,i):
            nonlocal sol
            if i == len(s):
                sol.append(arr[::])
            for j in range(i, len(s)):
                temp = s[i:j+1]
                if ispalindrome(temp):
                    arr.append(temp)
                    helper(s,arr, j + 1)
                    arr.pop()
        
        helper(s, [], 0)
        return sol
        


