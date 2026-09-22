from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        s1_counts = Counter(s1) 

        L = 0
        R = len(s1) - 1
        
        curr_counts = Counter(s2[L:R+1])

        while R < len(s2)-1:

            if curr_counts == s1_counts:
                return True

            R += 1
            curr_counts[s2[R]] = 1 + curr_counts.get(s2[R], 0)

            curr_counts[s2[L]] -= 1
            if curr_counts[s2[L]] == 0:
                del curr_counts[s2[L]]

            L += 1
            
        return curr_counts == s1_counts

