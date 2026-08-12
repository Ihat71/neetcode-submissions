class Solution:
    def isPalindrome(self, s: str) -> bool:
        punc = ['.', '?', '!', ',', ' ', "'", ':']
        for p in punc:
            s=s.replace(p, '')
        print(s)

        last_index = len(s) - 1


        for i in range(len(s)):
            if s[i].lower() != s[last_index - i].lower():
                return False

        return True