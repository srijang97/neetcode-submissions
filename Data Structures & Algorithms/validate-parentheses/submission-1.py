class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        bracket_map = {
            "}": "{",
            "]": "[",
            ")": "("
        }

        for bracket in s:
            
            if bracket in bracket_map:

                if len(stack) == 0 or stack[-1] != bracket_map[bracket]:
                    return False
                else:
                    stack.pop()

            else:
                stack.append(bracket)
        
        return len(stack) == 0





        
        