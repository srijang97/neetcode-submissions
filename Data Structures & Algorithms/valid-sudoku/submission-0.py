class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rowSets = [set() for _ in range(9)]
        colSets = [set() for _ in range(9)]
        subBoxSets = [set() for _ in range(9)]

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
                
                boxNumber = (i//3)*3 + (j//3)
                
                if board[i][j] in subBoxSets[boxNumber]:
                    return False
                else:
                    subBoxSets[boxNumber].add(board[i][j])

        return True
                

        