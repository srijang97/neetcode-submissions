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
        
        for root in adj_list:                                       
            if root not in visited:
                if root >= 1:
                    return False

                is_valid = dfs(root, visited, -1)
                if is_valid == False:
                    return False

        return True
