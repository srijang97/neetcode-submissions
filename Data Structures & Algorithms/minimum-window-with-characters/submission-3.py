from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        # t_freq = [0]*len(26)
        # s_freq = [0]*len(26)

        t_set = set(t)

        # for char in t:
        #     t_freq[ord(char)-ord('A')] += 1

        t_counter = Counter(t)
        s_counter = {}

        # matches = 0
        result = ""
        L = 0

        # for i in range(len(s)):

        #     if s[i] in t_set:
        #         L = i
        #         break

        # if L == None:
        #     return result

        # for R in range(L, L + len(t) - 1):
        #     s_counter[s[R]] = 1 + s_counter.get(s[R], 0)

        for R in range(len(s)):
            
            s_counter[s[R]] = 1 + s_counter.get(s[R], 0)

            found = True
            for k, v in t_counter.items():
                if k not in s_counter or s_counter[k] < v:
                    found = False
                    break
            
            while found == True:
                if result == "" or R-L+1 < len(result):
                    result = s[L:R+1]

                s_counter[s[L]] -= 1
                if s[L] in t_set and s_counter[s[L]] < t_counter[s[L]]:
                    found = False
                    L += 1
                    while L <= R and s[L] not in t_set:
                        s_counter[s[L]] -= 1
                        L += 1
                else:
                    L += 1

        return result

            
            
                
            

            
                

            
