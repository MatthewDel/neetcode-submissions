class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ideal_map = {}
        sol = float('inf')
        result = ""

        for char in t:
            ideal_map[char] = ideal_map.get(char, 0) + 1

        left = 0
        running_map = {}

        for right in range(len(s)):
            if s[right] in ideal_map:
                running_map[s[right]] = running_map.get(s[right], 0) + 1

            while left < right:
                if s[left] not in ideal_map:
                    left += 1
                elif running_map[s[left]] > ideal_map[s[left]]:
                    running_map[s[left]] -= 1
                    left += 1
                else:
                    break

            bad = False
            for key in ideal_map:
                if key not in running_map or running_map[key] < ideal_map[key]:
                    bad = True

            if not bad and (right - left + 1) < sol:
                sol = right - left + 1
                result = s[left: right + 1]
        
        print(sol)
        return result
            


