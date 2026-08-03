class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []
        out=[0]*len(temperatures)

        for index, temp in enumerate(temperatures):
            while(stack and temp > temperatures[stack[-1]]):
                i=stack.pop()
                out[i] = index - i
            stack.append(index)


        return out

        