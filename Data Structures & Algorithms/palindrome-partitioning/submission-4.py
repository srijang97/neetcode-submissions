class Solution:
    def partition(self, s: str) -> List[List[str]]:
        

        def is_palindrome(s, i, j):
            l, r = i, j
            while l < r:
                if s[l] != s[r]:
                    return False
                l, r = l+1, r-1
            return True
            

        res = []
        parts = []

        def dfs(i):
            if i >= len(s):
                res.append(parts.copy())
                return

            for j in range(i, len(s)):
                if is_palindrome(s, i, j):
                    parts.append(s[i:j+1])
                    dfs(j+1)
                    parts.pop()

        dfs(0)
        return res