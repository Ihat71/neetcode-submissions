class Solution:

    def largestRectangleArea(self, heights: List[int]) -> int:
        mono_stack = []
        max_area = 0
        len_h = len(heights)

        for i, h in enumerate(heights):
            last_popped=None
            while(mono_stack and mono_stack[-1][1] > h):
                popped = mono_stack.pop()
                area = popped[1] * (i - popped[0])
                last_popped = popped
                if area > max_area:
                    max_area = area
            index = last_popped[0] if last_popped and h < last_popped[1] else i
            mono_stack.append((index,h))


        for i, h in mono_stack:
            max_area = max(max_area, h * (len_h - i))
            

                
        return max_area
        