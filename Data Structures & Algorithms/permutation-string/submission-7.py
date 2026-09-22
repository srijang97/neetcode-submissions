class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False

        pattern = [0]*26
        window = [0]*26

        for p in s1:
            pattern[ord(p)-ord('a')] += 1

        left = 0

        for right, char in enumerate(s2):
            window[ord(char)-ord('a')] += 1

            if right -left + 1 > len(s1):
                window[ord(s2[left])-ord('a')] -= 1
                left += 1

            if  right -left + 1  == len(s1):
                if window == pattern:
                    return True

        return False
