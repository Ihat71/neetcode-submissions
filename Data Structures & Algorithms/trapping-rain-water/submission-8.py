class Solution:
    def trap(self, height: List[int]) -> int:
        # mono_stack_right = []
        # total = 0
        # j = len(height) - 1
        # for i, h in enumerate(height[::-1]):
        #     i = j - i
        #     if not mono_stack_right:
        #         mono_stack_right.append((i, h))
        #     elif mono_stack_right and h >= mono_stack_right[-1][1]:
        #         mono_stack_right.append((i, h))
        # max_left = 0
        # for i, h in enumerate(height):
        #     if h >= max_left:
        #         max_left = h
        #     while mono_stack_right and mono_stack_right[-1][0] <= i:
        #         mono_stack_right.pop()
        #     if mono_stack_right:
        #         answer = min(max_left, mono_stack_right[-1][1]) - h 
        #         total += answer if answer > 0 else 0
        total = 0
        i, j = 0, len(height) - 1
        left_max, right_max = height[i], height[j]
        while i < j:            
            if left_max < right_max:
                i+= 1
                left_max = max(left_max, height[i])
                total += left_max - height[i]
            else:
                j -= 1
                right_max = max(right_max, height[j])
                total+= right_max - height[j]

            

        return total