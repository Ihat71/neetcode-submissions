class Solution:
    def trap(self, height: List[int]) -> int:
        # mono_stack_left = []
        mono_stack_right = []
        total = 0

        # right = len(height) - 1
        # for i, h in enumerate(height):
        #     if not mono_stack_left:
        #         mono_stack_left.append((i, h))
        #     if mono_stack_left and h >= mono_stack_left[-1][1]:
        #         mono_stack_left.append((i, h))
        #     if mono_stack_right and height[right] >= mono_stack_right[-1][1]:
        #         mono_stack_right.append((i, height[right]))
        #     if not mono_stack_right:
        #         mono_stack_right.append((right, height[right]))
        #     elif mono_stack_left and h < mono_stack_left[-1][1]:
        #         left = mono_stack_left[-1][0]
        #         j = i + 1
        #         max_right = mono_stack_right[-1][1]
        #         while j < right:
        #             max_right = max(max_right, height[j])
        #             j += 1
        #         total += min(max_right, height[left]) - h

        #         print(i, h, left, right, total)
        #     right -= 1
        j = len(height) - 1
        for i, h in enumerate(height[::-1]):
            i = j - i
            if not mono_stack_right:
                mono_stack_right.append((i, h))
            elif mono_stack_right and h >= mono_stack_right[-1][1]:
                mono_stack_right.append((i, h))
        max_left = 0
        for i, h in enumerate(height):
            if h >= max_left:
                max_left = h
            while mono_stack_right and mono_stack_right[-1][0] <= i:
                mono_stack_right.pop()
            if mono_stack_right:
                total += min(max_left, mono_stack_right[-1][1]) - h if h < min(max_left, mono_stack_right[-1][1]) else 0
            # print(i, h, max_left, mono_stack_right, total)  


        return total