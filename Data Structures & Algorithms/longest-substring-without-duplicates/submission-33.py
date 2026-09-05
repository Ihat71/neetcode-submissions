class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # seen = {}
        # l, r = 0, 0
        # max_l = 0
        # while s and r<len(s):

        #     if s[r] not in seen:
        #         seen[s[r]] = r 

        #     elif r > l and s[r] in seen:
        #         new_pos = seen[s[r]] + 1
        #         l = new_pos if new_pos >= l else l
        #         seen[s[r]] = r
        #     max_l = max(max_l, r-l+1)

        #     r+=1
        # return max_l

        l = 0
        seen = set()
        res = 0

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l+=1
            seen.add(s[r])
            res = max(res, r-l+1)

        return res
