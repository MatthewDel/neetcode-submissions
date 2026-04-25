class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        tracing_set = set()
        pre_index = 0
        max_length = 0
        for i in range(len(s)):
            if s[i] in tracing_set:
                while pre_index < i:
                    if s[pre_index] == s[i]:
                        pre_index += 1
                        break 
                    else:
                        if s[pre_index] in tracing_set:
                            tracing_set.remove(s[pre_index])
                        pre_index +=1 
            else:
                tracing_set.add(s[i])
                max_length = max(max_length, i - pre_index + 1)     
        return max_length 
