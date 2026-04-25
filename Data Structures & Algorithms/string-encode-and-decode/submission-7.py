class Solution:

    def encode(self, strs: List[str]) -> str:
        sol = [] 
        for i in range(len(strs)):
            sol.append(str(len(strs[i])) + "#" + strs[i])
        print(sol)
        return ''.join(sol)

    def decode(self, s: str) -> List[str]:
        sol = []
        index = 0
        while index < len(s):
            number = 0
            while s[index] != '#':
                number = number * 10 + int(s[index])
                index += 1
            sol.append(s[index + 1: index + 1 + number])
            index = index + 1 + number
        return sol  
        # example: 4#neet4#code 
            
            
        print(s)