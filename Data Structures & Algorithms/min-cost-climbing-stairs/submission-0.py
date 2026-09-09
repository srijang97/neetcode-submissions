class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        

        if cost[0] < cost[1]:
            step_costs = [0, cost[0]]
            next_step = 2
        else:
            step_costs = [0, cost[1]]
            next_step = 3

        for i in range(3, len(cost)):
            
            temp = step_costs[1]

            step_costs[1] = min(step_costs[0] + cost[i-2], step_costs[1] + cost[i-1])

            step_costs[0] = temp

        return min(step_costs[-1] + cost[-1], step_costs[-2] + cost[-2])