class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0

        i, j = 0, len(heights) - 1

        while i < j:

            max_area = max(min(heights[i], heights[j]) * (j - i), max_area)

            if heights[j] < heights[i]:
                j -= 1
            elif heights[i] <= heights[j]:
                i += 1

            # elif heights[i] == heights[j]:
            #     if heights[i+1] < heights[j-1]:
            #         heights[j] -= 1
            #     else:
            #         heights[i] += 1

            

        return max_area