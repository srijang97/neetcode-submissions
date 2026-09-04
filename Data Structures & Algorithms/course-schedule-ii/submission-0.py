class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
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

        courses_taken = []
    
        while queue:

            curr = queue.popleft()
            courses_taken.append(curr)
            
            for n in adj_list[curr]:
                indegrees[n] -= 1
                if indegrees[n] == 0:
                    queue.append(n)
            
        return courses_taken if len(courses_taken) == numCourses else []