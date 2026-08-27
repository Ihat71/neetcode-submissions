class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k_up = max(piles)
        l, r = 1, k_up
        min_k = k_up
        while l<=r:
            mid = (r+l) // 2
            time = 0
            for pile in piles:
                time+= self.ceilDiv(pile, mid)

            if time <= h:
                min_k = mid
                r = mid - 1
            elif time > h:
                l = mid + 1



        return min_k


    
    def ceilDiv(self, a, b):
        return -(-a//b)

