from math import floor
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hashmap = {}
        sol = []
        n = len(nums)
        for i in range(n):
            if nums[i] not in hashmap:
                if len(hashmap) == 2:
                    delete = []
                    for key in hashmap:
                        if hashmap[key] == 1:
                            delete.append(key)
                        else:
                            hashmap[key] -= 1
                    for key in delete:
                        del hashmap[key]
                else:
                    hashmap[nums[i]] = 1
            else:
                hashmap[nums[i]] += 1
        
    
        for key in hashmap:
            count = 0
            for num in nums:
                if num == key:
                    count += 1
                    if count > floor(n / 3):
                        sol.append(key)
                        break
        
        return sol 
                

