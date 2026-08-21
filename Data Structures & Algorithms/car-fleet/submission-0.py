from collections import OrderedDict

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        stack = []         
        
        hrs_to_target = {}

        for i, p in enumerate(position):
            hrs_to_target[p] = (target - p)/speed[i]

        sorted_dict = OrderedDict(sorted(hrs_to_target.items(), key=lambda item: item[0]))

        for car in sorted_dict:

            while len(stack) > 0 and sorted_dict[car] >= sorted_dict[stack[-1]]:
                stack.pop()

            stack.append(car)

        return len(stack)

