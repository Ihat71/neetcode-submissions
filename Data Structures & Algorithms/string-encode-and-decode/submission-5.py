class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for word in strs:
            ans += str(len(word)) + "#" + word
        return ans

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0
        while i < len(s):
            arr = ""
            index = s.find("#", i)
            length = int(s[i:index])
            arr += s[index+1:index+length+1]
            ans.append(arr)
            i = index + length + 1
        return ans
