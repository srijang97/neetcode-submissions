class Solution:
    def trap(self, height: List[int]) -> int:

        maxHeightsLeft  = [0] * len(height)
        maxHeightsRight  = [0] * len(height)

        for i in range(1, len(height)):

            maxHeightsLeft[i] = max(maxHeightsLeft[i-1], height[i-1])

        for i in range(len(height)-2, -1, -1):

            maxHeightsRight[i] = max(maxHeightsRight[i+1], height[i+1])
        
        # print(maxHeightsLeft)
        # print(maxHeightsRight)
        result = 0
        for i, h in enumerate(height):

            heightDiff = min(maxHeightsLeft[i], maxHeightsRight[i]) - h
            result += heightDiff if heightDiff > 0 else 0

        return result



            
        