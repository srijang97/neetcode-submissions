class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:

        # Your code goes here
        adj_list = {}
        if source == target:
            return 0
        for i, route in enumerate(routes):
            for j in range(len(route)):
                if route[j] in adj_list:
                    adj_list[route[j]] += [(i, x) for x in route if x!=route[j]]
                else:
                    adj_list[route[j]] = [(i, x) for x in route if x!=route[j]]

        queue = deque([])

        visited = set()
        visited.add(source)

        if target not in adj_list or source not in adj_list:
            return -1

        for stop in adj_list[source]:
            if stop[1] == target:
                return 1

            queue.append((*stop, 1))
            visited.add(stop)

        while queue:

            bus_no, stop, changes = queue.popleft()

            if stop == target:
                return changes

            for bus, dest in adj_list[stop]:

                if dest not in visited: 
                    
                    this_dest_change = 0
                    if bus_no != bus:
                        this_dest_change += 1
                    
                    visited.add(dest)
                    queue.append((bus, dest, changes + this_dest_change))

        return -1

        