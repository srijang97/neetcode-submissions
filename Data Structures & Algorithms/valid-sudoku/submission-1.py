class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rowSets = [set() for _ in range(9)]
        colSets = [set() for _ in range(9)]
        boxSets = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                    
                if board[i][j] in rowSets[i]:
                    return False
                else:
                    rowSets[i].add(board[i][j])

                if board[i][j] in colSets[j]:
                    return False
                else:
                    colSets[j].add(board[i][j]) 

                boxNumber = 3*(i // 3) + (j // 3) 

                if board[i][j] in boxSets[boxNumber]:
                    return False
                else:
                    boxSets[boxNumber].add(board[i][j])  

        return True
