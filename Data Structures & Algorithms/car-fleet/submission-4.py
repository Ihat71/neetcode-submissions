class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        last_time = None
        count=0

        vector_list = list(zip(position, speed))
        vector_list.sort(key=lambda tup: tup[0], reverse=True)

        for x in vector_list:
            time = (target-x[0]) / x[1]
            if last_time:
                if time <= last_time:
                    continue
                else:
                    last_time = time
                    count += 1
            if not last_time:
                last_time = time
                count+=1


        return count