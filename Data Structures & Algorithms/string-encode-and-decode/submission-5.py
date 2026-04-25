class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            res += str(len(string)) + "#" + string
        return res 

    def decode(self, s: str) -> List[str]:
        i = 0 
        sol = []
        if len(s) == 1:
            return []
        while i < len(s):
            runningLength = 0
            while s[i] != "#":
                runningLength = runningLength * 10 + int(s[i])
                i+=1 
            sol.append(s[i+1: i+1+runningLength])
            i = i+1+runningLength
        return sol

            
