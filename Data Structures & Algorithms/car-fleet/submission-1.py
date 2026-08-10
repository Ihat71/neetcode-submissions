class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car_fleet = []
        count=0

        vector_list = [(x, speed[i]) for i, x in enumerate(position)]

        sorted_list = sorted(vector_list, key=lambda tup: tup[0], reverse=True)

        for x in sorted_list:
            time = (target-x[0]) / x[1]
            if car_fleet:
                if time <= car_fleet[0]:
                    car_fleet.append(time)
                else:
                    while(car_fleet):
                        car_fleet.pop()
                    car_fleet.append(time)
                    count += 1
            if not car_fleet:
                car_fleet.append(time)
                count+=1


        return count