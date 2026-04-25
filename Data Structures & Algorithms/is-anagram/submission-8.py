class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        n = len(s)
        m = len(t)

        if m != n:
            return False 

        hash_map = [0] * 26

        for i in range(n):
            hash_map[ord(s[i]) - ord('a')] += 1
            hash_map[ord(t[i]) - ord('a')] -= 1

        for i in range(len(hash_map)):
            if hash_map[i] != 0:
                return False
        
        return True 
        