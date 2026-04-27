class Solution:
    def complete(self, hashmap):
        all_zero = True 

        for value in hashmap.values():
            if value != 0:
                all_zero = False
        
        return all_zero 

    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False 
        
        chars_in_s1 = defaultdict(int)

        for char in s1:
            chars_in_s1[char] += 1

        left = 0 
        for i in range(len(s2)):
            if s2[i] in chars_in_s1:
                chars_in_s1[s2[i]] -= 1

                print(chars_in_s1)
                if self.complete(chars_in_s1):
                    return True 

                while left < i and chars_in_s1[s2[i]] < 0:
                    chars_in_s1[s2[left]] += 1
                    left += 1
            else:
                while left < i + 1:
                    if s2[left] in chars_in_s1:
                        chars_in_s1[s2[left]] += 1
                    left += 1 

        return False

        