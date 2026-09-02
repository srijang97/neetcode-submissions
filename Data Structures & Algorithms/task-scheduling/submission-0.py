from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        cnts = Counter(tasks)
        heap = []

        for task in cnts:
            heap.append(-cnts[task])
        
        heapq.heapify(heap)
        task_queue = deque()

        time = 0

        while heap or task_queue:
            time += 1
            if heap:
                curr_task = heapq.heappop(heap)

                if curr_task + 1 != 0:
                    task_queue.append((curr_task+1, time+n))

            if task_queue:
                if task_queue[0][1] == time:
                    heapq.heappush(heap, task_queue.popleft()[0])

        return time





