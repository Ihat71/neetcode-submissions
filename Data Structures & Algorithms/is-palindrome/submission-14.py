class Solution:
    def isPalindrome(self, s: str) -> bool:
        # punc = ['.', '?', '!', ',', ' ', "'", ':', ';', '"', '|']
        # for p in punc:
        #     s=s.replace(p, '')

        # last_index = len(s) - 1


        # for i in range(len(s)):
        #     if s[i].lower() != s[last_index - i].lower():
        #         return False

        # return True
        i=0
        j=len(s) - 1
        while(i <= j and i < len(s) - 1 and j >= 0):
            if s[i].isalnum() and s[j].isalnum():
                if s[i].lower() != s[j].lower():
                    return False
                else:
                    i+=1
                    j-=1
            if not s[i].isalnum():
                i+=1
            if not s[j].isalnum():
                j-=1

        return True