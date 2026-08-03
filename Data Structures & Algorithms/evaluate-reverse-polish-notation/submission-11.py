class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = ['+', '-', '/', '*']

        stack = []

        for token in tokens:
            if token in ops:
                y = stack.pop()
                x = stack.pop()
                print(x, token, y)
                safe_dict={'y': y, 'x': x}
                expr = 'x' + token + 'y'
                res = eval(expr, {}, safe_dict)
                stack.append(int(res))


            else:
                stack.append(int(token))

        return stack.pop()