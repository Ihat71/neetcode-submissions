class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ''
        encoded = ""
        for s in strs:
            if s == '':
                s = " "
            new_s = s + "jkbnh"
            encoded = encoded + new_s 
        return encoded

    def decode(self, s: str) -> List[str]:
        if s == '':
            return []
        last_index = 0
        res = []
        len_s = len(s)
        for index in range(len_s - 1):
            print(s[index+1:index+5])
            if s[index+1:index+6] == "jkbnh":
                if s[last_index:index+1] != " ":
                    res.append(s[last_index:index+1])
                else:
                    res.append('')
                last_index = index + 6 
        print(last_index)

        if not res:
            res.append('')
        return res

