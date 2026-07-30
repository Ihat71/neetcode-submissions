class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        test = []

        s = list(s)
        t = list(t)

        for i in s:
            for j in t:
                if i == j:
                    test.append(1)
                    t.remove(j)
                    break
                
        
        if len(test) == len(s):
            return True
        else:
            return False

                    