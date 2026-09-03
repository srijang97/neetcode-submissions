class Solution:
    def solve(self, board: List[List[str]]) -> None:

        if not board:
            return
        
        rows = len(board)
        cols = len(board[0])

        visited = set()

        def dfs(r, c):

            if r < 0 or r >=rows or c < 0 or c >= cols or (r,c) in visited or board[r][c] == 'X':
                return
            
            visited.add((r,c))
            board[r][c] = 'S'

            directions = [(0,1), (0,-1), (1,0), (-1,0)]

            for d in directions:
                dfs(r+d[0], c+d[1])
            
            return

        for r in [0, rows-1]:
            for c in range(cols):
                if board[r][c] == 'O' and (r,c) not in visited:
                    dfs(r,c)
        
        for r in range(rows):
            for c in [0, cols-1]:
                if board[r][c] == 'O' and (r,c) not in visited:
                    dfs(r,c)

        for r in range(rows):
            for c in range(cols):

                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'S':
                    board[r][c] = 'O'

        return

        