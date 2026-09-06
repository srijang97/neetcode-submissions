class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        graph = {}
        
        for u, v, price in flights:
            if u not in graph:
                graph[u] = []
            graph[u].append((v, price))

        distances = {(src, 0): 0}

        heap = [(0, src, 0)]

        while heap:

            dist, node, stops = heapq.heappop(heap)

            if node == dst:
                return dist

            if node not in graph:
                continue

            if stops == k+1:
                continue

            if dist > distances.get(node, float("inf")):
                continue

            for n, p in graph[node]:

                if dist + p < distances.get((n, stops+1), float("inf")):
                    distances[(n, stops+1)] = dist + p
                    heapq.heappush(heap, (dist+p, n, stops+1))

        return -1
        