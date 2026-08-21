
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        stack = []         
        
        cars = sorted((p, (target-p)/speed[i]) for i, p in enumerate(position))

        for car in cars:

            while len(stack) > 0 and car[1] >= stack[-1][1]:
                stack.pop()

            stack.append(car)

        return len(stack)

