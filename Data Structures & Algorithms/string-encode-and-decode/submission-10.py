class Solution:

    def encode(self, strs: List[str]) -> str:
        
        encodedStr = ""

        for s in strs:
            encodedStr += str(len(s)) + '#' + s

        return encodedStr

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []

        print(s)
        i = j = 0

        res = []

        while j < len(s):

            while s[j] != '#':
                j += 1
            

            str_length = int(s[i:j])
            if str_length > 0:
                res.append(s[j+1:j+1+str_length])
            else:
                res.append("")

            j += 1+str_length
            i = j

        return res