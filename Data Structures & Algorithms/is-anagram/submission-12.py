class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)): 
            return False
        
        hashmap = [0] * 26

        for i in range(len(s)):
            hashmap[ord(s[i]) - ord('z')] += 1
            hashmap[ord(t[i]) - ord('z')] -= 1
        
        for num in hashmap:
            if num != 0:
                return False
        
        return True