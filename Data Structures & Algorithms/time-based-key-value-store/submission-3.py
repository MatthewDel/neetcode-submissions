class TimeMap:

    def __init__(self):
        self.hash_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hash_map:
            self.hash_map[key] = [(value,timestamp)]
        else:
            self.hash_map[key].append((value,timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        
        if key not in self.hash_map or self.hash_map[key] == []:
            return ""
        
        left = 0 
        right = len(self.hash_map[key])-1
        while left<=right:
            mid = (left + right) // 2
            if self.hash_map[key][mid][1] == timestamp:
                return self.hash_map[key][mid][0]
            elif self.hash_map[key][mid][1] < timestamp:
                left = mid + 1
            else:
                right = mid - 1
        if self.hash_map[key][right][1] > timestamp:
            return ""
        return self.hash_map[key][right][0]

    