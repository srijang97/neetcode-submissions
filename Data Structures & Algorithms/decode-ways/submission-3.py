class Solution:
    def numDecodings(self, s: str) -> int:
        
        if s[0] == '0':
            return 0

        dp0 = 1
        dp1 = 1

        for i in range(2, len(s)+1):

            curr_ways = 0 

            if s[i-1] != '0':
                curr_ways += dp1

            if 10 <= int(s[i-2:i]) <= 26:
                curr_ways += dp0

            dp0 = dp1
            dp1 = curr_ways

        return dp1