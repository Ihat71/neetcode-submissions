class Solution:
    def getTime(self, target, d, s):
        return (target - d) / s
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        last_time = 0
        count=0

        vector_list = list(zip(position, speed))
        vector_list.sort(key=lambda tup: tup[0], reverse=True)

        for d, s in vector_list:
            time = self.getTime(target, d, s)
            if time > last_time:
                count += 1
                last_time = time


        return count