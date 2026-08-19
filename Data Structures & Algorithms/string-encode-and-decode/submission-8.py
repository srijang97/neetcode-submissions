class Solution:

    def encode(self, strs: List[str]) -> str:
        
        base_str = ""

        for s in strs:
            base_str += f"{str(len(s))}#{s}"
        
        print(base_str)
        return base_str

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []

        ans = []

        i = 0  
        while i < len(s):
            
            curr_string = ""  
            curr_str_length = ""

            while s[i] != '#':
                curr_str_length += s[i]
                i += 1

            str_end = i + int(curr_str_length)
            while i < str_end:
                i += 1
                curr_string += s[i]
            
            ans.append(curr_string)
            i += 1
        
        return ans