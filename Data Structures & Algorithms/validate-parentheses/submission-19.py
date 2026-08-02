class Solution:
    def isValid(self, s: str) -> bool:
        paran_hash = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }

        stack = [-1]

        for c in s:
            if c in paran_hash and stack:
                closing_c = stack.pop()
                if closing_c != paran_hash[c] or closing_c == -1:
                    return False
            else:
                stack.append(c) 
        return True if stack == [-1] else False
        