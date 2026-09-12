class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        # Your code goes here
        memo = {}

        wordSet = set(wordDict)

        def dfs(i):

            if i in memo:
                return memo[i]

            if i == len(s):
                return True

            for j in range(i+1, len(s)+1):
                if s[i:j] in wordSet:
                    if dfs(j) == True:
                        memo[i] = True
                        return True

            memo[i] = False
            return memo[i]

        return dfs(0)
