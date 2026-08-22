class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack = []
        maxArea = float("-inf")

        for i in range(len(heights)):
            
            lastPoppedIdx = i
            while len(stack) > 0 and heights[i] < stack[-1][1]:
                elem = stack.pop()
                maxArea = max(maxArea, (i-elem[0])*elem[1])
                lastPoppedIdx = elem[0]
            
            stack.append((lastPoppedIdx, heights[i]))

        while stack:
            elem = stack.pop()
            maxArea = max(maxArea, (len(heights)-elem[0])*elem[1])

        return maxArea



