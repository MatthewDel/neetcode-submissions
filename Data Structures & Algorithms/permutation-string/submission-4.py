class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)
        if n > m:
            return False 
        chars = {}

        for i in range(n):
            if s1[i] in chars:
                chars[s1[i]] += 1 
            else:
                chars[s1[i]] = 1 
        
        running_chars = {}
        max_length = 0
        left = 0
        for right in range(m):
            if s2[right] not in chars:
                left = right + 1
                running_chars.clear()
            else:
                if s2[right] in running_chars:
                    if running_chars[s2[right]] == chars[s2[right]]:
                        while left < right:
                            if s2[left] == s2[right]:
                                left +=1
                                break 
                            running_chars[s2[left]] -= 1
                            left += 1
                    else:
                        running_chars[s2[right]] += 1
                else:
                    running_chars[s2[right]] = 1
            print(running_chars)
            if running_chars == chars:
                return True
        return False
            
