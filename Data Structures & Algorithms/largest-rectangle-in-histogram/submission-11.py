class Solution:
    def get_max_area(self, popped, i):
        return popped[1] * (i - popped[0])

    def largestRectangleArea(self, heights: List[int]) -> int:
        mono_stack = []
        max_area = 0
        len_h = len(heights)

        for i, h in enumerate(heights):
            count=None
            while(mono_stack and mono_stack[-1][1] > h):
                popped = mono_stack.pop()
                area = self.get_max_area(popped, i)
                count = popped
                if area > max_area:
                    max_area = area
            index = count[0] if count and h < count[1] else i
            mono_stack.append((index,h))


        for i, h in mono_stack:
            area = h * (len_h - i)
            if area > max_area:
                max_area = area

                
        return max_area
        