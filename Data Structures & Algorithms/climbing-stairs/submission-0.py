class Solution:
    def climbStairs(self, n: int) -> int:

        
        steps = [1, 1]

        for i in range(2, n+1):

            temp = steps[1]
            steps[1] = steps[1] + steps[0]
            steps[0] = temp

        return steps[1]


        