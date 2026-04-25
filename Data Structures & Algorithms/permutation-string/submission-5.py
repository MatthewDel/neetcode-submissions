class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ideal_set = defaultdict(int)
        for i in range(len(s1)):
            ideal_set[s1[i]] += 1

        curr_index = 0
        hash_set = defaultdict(int)
        for i in range(len(s2)):
            if s2[i] in ideal_set:
                hash_set[s2[i]] += 1 
                while curr_index < i and hash_set[s2[i]] > ideal_set[s2[i]]:
                    hash_set[s2[curr_index]] -= 1
                    curr_index += 1
                if hash_set == ideal_set:
                    return True
            else:
                hash_set = defaultdict(int)
                curr_index = i + 1
        
        return False 
