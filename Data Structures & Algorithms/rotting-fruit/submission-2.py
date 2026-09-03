from collections import deque

class Solution:

    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0]) 

        fresh_oranges = 0

        rotting = deque([])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    rotting.append((r, c))
                elif grid[r][c] == 1:
                    fresh_oranges += 1

        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        time = 0

        while rotting and fresh_oranges>0:
            time += 1
            n_rotting = len(rotting)

            for _ in range(n_rotting):

                x, y = rotting.popleft()                    

                for dr, dc in directions:

                    if (0<= x+dr<rows) and (0<= y+dc<cols) and grid[x+dr][y+dc] == 1:
                        rotting.append((x+dr, y+dc))
                        grid[x+dr][y+dc] = 2
                        fresh_oranges -= 1

                

        if fresh_oranges == 0:
            return time
        else:
            return -1


                        



