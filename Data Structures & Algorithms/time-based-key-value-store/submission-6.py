class TimeMap:

    def __init__(self):
        self.time_map = dict()
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        key = key.lower()
        value = value.lower()
        if key not in self.time_map:
            self.time_map[key] = [(timestamp, value)]
        else:
            self.time_map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        
        if key in self.time_map:
            values = self.time_map[key]
        else:
            return ""


        l, r = 0, len(values) - 1
        max_temp = 0
        val = ''
        while l<=r:
            
            mid = l + (r-l) // 2

            if values[mid][0] == timestamp:
                return values[mid][1]

            if values[mid][0] < timestamp and values[mid][0] >= max_temp:
                max_temp = values[mid][0]
                val = values[mid][1]
            
            if timestamp > values[mid][0]:
                l = mid + 1
            else:
                r = mid - 1

        #in here, if the last one didnt return nothing, we have to loop again to find the first value with a timestamp 
        #smaller than the timestamp and return that one

        # l, r = 0, len(values) - 1
        # max_temp = 0
        # val = ''
        # while l<=r:
            
        #     mid = l + (r-l) // 2

        #     if values[mid][0] < timestamp and values[mid][0] >= max_temp:
        #         max_temp = values[mid][0]
        #         val = values[mid][1]
        #     if timestamp > values[mid][0]:
        #         l = mid + 1
        #     elif timestamp < values[mid][0]:
        #         r = mid - 1

        return val
            


