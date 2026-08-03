class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []
        out=[0]*len(temperatures)

        for index, temp in enumerate(temperatures):
            # if not stack:
            #     stack.append(temp)
            if stack and temp >= stack[-1][0]:
                count=0
                while(stack and temp > stack[-1][0]):
                    x,i=stack.pop()
                    out[i] = index - i
                stack.append((temp, index))
            else:
                stack.append((temp, index))

        return out

        