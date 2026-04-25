class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_map = {}
        for i in range(len(s)):
            if s[i] in hash_map:
                hash_map[s[i]]+=1
            else:
                hash_map[s[i]]=1
        for j in range(len(t)):
            if t[j] not in hash_map or hash_map[t[j]]==0:
                return False
            hash_map[t[j]]-=1
       
        for key in hash_map:
            if hash_map[key] != 0:
                return False 
        
        return True