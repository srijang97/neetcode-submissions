class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        L = 0
        charSet = set()
        maxLen= 0
        for R in range(len(s)):
            
            while s[R] in charSet:
                charSet.remove(s[L])
                L += 1

            charSet.add(s[R])         
            maxLen = max(R-L+1, maxLen)
            
        return maxLen