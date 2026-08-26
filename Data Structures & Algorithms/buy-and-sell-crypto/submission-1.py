class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxProfit = 0
        L = 0

        for R in range(1, len(prices)):

            if prices[R] < prices[L]:
                L = R
            else:
                maxProfit = max(maxProfit, (prices[R]-prices[L]))
        
        return maxProfit


