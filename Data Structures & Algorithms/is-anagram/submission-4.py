class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_set = {}

        for i in range(len(s)):
            if s[i] in hash_set:
                hash_set[s[i]]+=1 
            else:
                hash_set[s[i]]=1
        
        for j in range(len(t)):
            if t[j] in hash_set and hash_set[t[j]] > 0:
                hash_set[t[j]]-=1 
            else:
                return False

        for key in hash_set:
            if hash_set[key] != 0:
                return False
        
        return True