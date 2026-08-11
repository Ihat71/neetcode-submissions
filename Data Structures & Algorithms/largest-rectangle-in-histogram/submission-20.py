class Solution:

    def largestRectangleArea(self, heights: List[int]) -> int:
        mono_stack = []
        max_area = 0
        len_h = len(heights)

        for i, h in enumerate(heights):
            start=i
            while(mono_stack and mono_stack[-1][1] > h):
                popped = mono_stack.pop()
                area = popped[1] * (i - popped[0])
                start=popped[0]
                max_area = max(area, max_area)

            mono_stack.append((start,h))


        for i, h in mono_stack:
            max_area = max(max_area, h * (len_h - i))
            

                
        return max_area
        