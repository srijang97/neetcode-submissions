class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        L = 0

        hashMap = {}

        max_f = 0

        max_len = 0

        for R in range(len(s)):
            
            f = hashMap.get(s[R], 0)
            max_f = max(max_f, f+1)

            if s[R] in hashMap:
                hashMap[s[R]] += 1
            else:
                hashMap[s[R]] = 1            

            

            while (R - L + 1) - max_f > k:

                hashMap[s[L]] -= 1
                L += 1            

            max_len = max(R-L+1, max_len)
            
        return max_len