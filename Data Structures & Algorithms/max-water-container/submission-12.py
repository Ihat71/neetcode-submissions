class Solution:
    def getArea(self, heights, i, j):
        return min(heights[i], heights[j]) * (j - i)
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0

        i, j = 0, len(heights) - 1

        while i < j:

            if self.getArea(heights, i, j) > max_area:
                max_area = self.getArea(heights, i, j)

            if heights[j] < heights[i]:
                j -= 1
            # elif heights[i] < heights[j]:
            #     i += 1
            else:
                i +=1
            # elif heights[i] == heights[j]:
            #     if heights[i+1] < heights[j-1]:
            #         heights[j] -= 1
            #     else:
            #         heights[i] += 1

            

        return max_area