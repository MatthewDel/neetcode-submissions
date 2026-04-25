class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for i in range(len(strs)):
            string+=str(len(strs[i]))+"#"
            string+=strs[i]
        
        return string
    
    def decode(self, strs):
        
        n = len(strs)
        if n == 1:
            return [""]

        i = 0
        sol = []

        while i<n:
            runningLength = 0
            while strs[i] != "#":
                runningLength = runningLength * 10 + int(strs[i])
                i += 1 
            
            i += 1
            temp = ""
            for j in range(runningLength):
                temp += (strs[i + j])
            sol.append(temp)
            
            
            i += runningLength
            
            
            
            
        print(sol)
        return sol

