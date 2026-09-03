class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        rows = len(board)
        cols = len(board[0])
        
        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        def dfs(r, c, i):
            
            if i == len(word):
                return True

            if r < 0 or r >= rows or c <0 or c >= cols or board[r][c] != word[i]:
                return False

            

            temp = board[r][c]
            board[r][c] = '#'

            found = False

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                found = found or dfs(nr, nc, i+1)
            
            board[r][c] = temp
            
            return found

        for r in range(rows):
            for c in range(cols):

                if board[r][c] == word[0]:
                    if dfs(r, c, 0):
                        return True

        return False
