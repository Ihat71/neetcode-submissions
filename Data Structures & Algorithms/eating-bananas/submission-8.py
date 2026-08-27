class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        min_k = r
        while l<=r:
            mid = (r+l) // 2
            time = 0
            for pile in piles:
                time+= -(-pile//mid)

            if time <= h:
                min_k = mid
                r = mid - 1
            elif time > h:
                l = mid + 1

        return min_k




