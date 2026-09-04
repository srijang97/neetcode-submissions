class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        result = []

        def backtrack(open_count, close_count, string):

            if len(string) == 2*n:
                result.append(string)
                return

            if open_count < n:
                backtrack(
                    open_count+1,
                    close_count,
                    string + "("
                )
            if close_count < open_count:
                backtrack(
                    open_count,
                    close_count+1,
                    string+")"
                )

            return

        backtrack(0, 0, "")

        return result