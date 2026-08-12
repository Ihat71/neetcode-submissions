class Solution:
    def isPalindrome(self, s: str) -> bool:
        punc = ['.', '?', '!', ',', ' ', "'", ':']
        for p in punc:
            s=s.replace(p, '')
        s=s.lower()
        print(s)

        last_index = len(s) - 1


        for i, c in enumerate(s):
            if c != s[last_index - i]:
                return False

        return True