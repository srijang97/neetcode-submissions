from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj_list = [[] for _ in range(numCourses)]

        for pre in prerequisites:
            adj_list[pre[1]].append(pre[0])

        indegrees = {i: 0 for i in range(numCourses)}

        for i in range(numCourses):
            for n in adj_list[i]:
                indegrees[n] = indegrees.get(n, 0) + 1
        
        queue = deque()

        for node in indegrees:
            if indegrees[node] == 0:
                queue.append(node)

        courses_taken = 0
    
        while queue:

            curr = queue.popleft()
            courses_taken += 1
            
            for n in adj_list[curr]:
                indegrees[n] -= 1
                if indegrees[n] == 0:
                    queue.append(n)
            
        return courses_taken==numCourses



            