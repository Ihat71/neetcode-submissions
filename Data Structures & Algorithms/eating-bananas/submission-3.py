class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k_up = max(piles)
        k_low = 1

        # sols = [x for x in range(k_low, k_up + 1)]

        l, r = k_low, k_up
        min_k = k_up
        while l<=r:
            mid = (r+l) // 2
            time = 0
            for pile in piles:
                time+= self.ceilDiv(pile, mid)
            # print(min_k, l, r, mid, time, sols)

            if time <= h:
                min_k = mid
                r = mid - 1
            elif time > h:
                l = mid + 1



        return min_k


    
    def ceilDiv(self, a, b):
        return -(-a//b)

