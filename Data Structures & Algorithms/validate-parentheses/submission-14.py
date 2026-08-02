class Solution:
    def isValid(self, s: str) -> bool:
        paran_hash = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }
        paran_hash_2 = {
            '(' : ')',
            '[' : ']',
            '{' : '}'
        }


        stack = [-1]

        for c in s:
            if c in paran_hash and stack:
                closing_c = stack.pop()
                if closing_c != paran_hash[c] or closing_c == -1:
                    return False
            else:
                stack.append(c) 
            if c in paran_hash_2:
                if paran_hash_2[c] not in s:
                    return False
            print(stack)
        if stack != [-1]:
            return False


        return True
        