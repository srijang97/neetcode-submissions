class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        countMap = {}

        for i in range(len(s)):

            if s[i] in countMap:
                countMap[s[i]] += 1
            else:
                countMap[s[i]] = 1

            if t[i] in countMap:
                countMap[t[i]] -= 1
            else:
                countMap[t[i]] = -1

        for v in countMap.values():
            if v != 0:
                return False
        
        return True
        