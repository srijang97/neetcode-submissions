from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adj_list = defaultdict(list)
        

        for u, v, w in times:
            adj_list[u].append((v, w))

        distances = {}

        distances[k] = 0

        heap = [(0, k)]

        while heap:

            dist, node = heapq.heappop(heap)

            if dist > distances.get(node, float('inf')):
                continue

            for v, w in adj_list[node]:

                if dist + w < distances.get(v, float("inf")):
                    distances[v] = dist + w
                    heapq.heappush(heap, (dist+w, v))
        
        if len(distances) != n:
            return -1

        return max(distances.values())

                