class TimeMap:

    def __init__(self):
        self.time_store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        value_store = self.time_store[key]

        if not value_store:
            return ""

        left = 0
        right = len(value_store) - 1 

        while left <= right:
            mid = (left + right) // 2 
            temp_timestamp = value_store[mid][1]

            if temp_timestamp > timestamp:
                right = mid - 1
            elif temp_timestamp < timestamp:
                left = mid + 1 
            else:
                return value_store[mid][0]
        
        if right >= 0:
            return value_store[right][0]
        else: 
            return ""
        

        #Binary Search on the timestamp
            #One: If i find it, then I just subtract one 
            #Two: If i dont find it, then I need to investigate the way the indexes finish. I believe that will be right
        

        
