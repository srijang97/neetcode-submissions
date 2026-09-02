class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        adj_list = {i: [] for i in range(n)}

        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        visited = set()

        def dfs(root, visited, parent):
            if root in visited:
                return False
            
            visited.add(root)
            
            for neigh in adj_list[root]:
                if neigh != parent:

                    is_valid = dfs(neigh, visited, root)
                    if is_valid == False:
                        return False
                
            return True
        
        is_valid = dfs(0, visited, -1)

        if is_valid == False or len(visited)!=len(adj_list):
            return False
        
        return True
