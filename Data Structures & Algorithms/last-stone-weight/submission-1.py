import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        stone_heap = stones
        heapq.heapify_max(stone_heap)

        while len(stone_heap) > 1:

            first = heapq.heappop_max(stone_heap)
            second = heapq.heappop_max(stone_heap)

            if first == second:
                pass
            elif first > second:
                heapq.heappush_max(stone_heap, first-second)
            else:
                heapq.heappush_max(stone_heap, second-first)

        return stone_heap[0] if stone_heap else 0

            
        