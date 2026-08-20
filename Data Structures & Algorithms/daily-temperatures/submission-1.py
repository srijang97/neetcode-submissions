class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = [(temperatures[0], 0)]

        result = [0]*len(temperatures)

        for day in range(1, len(temperatures)):

            while len(stack) > 0 and temperatures[day] > stack[-1][0]:

                popped_day = stack.pop()
                result[popped_day[1]] = day - popped_day[1]

            stack.append((temperatures[day], day))

        # while stack:
        #     popped_day = stack.pop()
        #     result[popped_day[1]] = 0

        return result