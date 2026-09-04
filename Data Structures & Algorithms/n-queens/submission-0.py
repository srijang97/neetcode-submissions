class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        res = []

        def is_valid_cell(i, j, board):
            for col in range(0, j):
                if board[i][col] == 'Q':
                    return False

            r, c = i-1, j-1

            while r >=0 and c >= 0:
                if board[r][c] == 'Q':
                    return False
                r, c = r-1, c-1

            r,c = i+1 , j-1
            while r < n and c >= 0:
                if board[r][c] == 'Q':
                    return False
                r, c = r+1, c-1

            return True
        
        def backtrack(c, board):

            if c == n:
                res.append(["".join(row) for row in board])
                return
            
            for r in range(n):
                if is_valid_cell(r, c, board):
                    board[r][c] = 'Q'
                    backtrack(c+1, board)
                    board[r][c] = '.'

        board = [['.']*n for _ in range(n)]

        backtrack(0, board)
        
        # for i, solution in enumerate(res):

        #     res[i] = ["".join(x) for x in solution]

        return res