class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = ['+', '-', '/', '*']

        stack = []

        for token in tokens:
            if token in ops:
                y = str(stack.pop())
                x = str(stack.pop())
                print(x, token, y)
                res = eval(token.join([x, y]))
                stack.append(int(res))


            else:
                stack.append(int(token))

        return stack.pop()