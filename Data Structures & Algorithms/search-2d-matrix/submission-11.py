class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        rows = len(matrix)
        cols = len(matrix[0])

        total = rows * cols

        def get_row_col_from_idx(idx):

            return (idx // cols, idx % (cols))

        L, R = 0, total - 1

        while  L <= R:
            mid = (L + R) // 2
            
            print(mid)
            r, c = get_row_col_from_idx(mid)
            
            print(f"{r}, {c}")

            if r < rows and c < cols:

                if target > matrix[r][c]:
                    print("greater")
                    L = mid + 1

                elif target < matrix[r][c]:
                    print("lesser")
                    R = mid - 1

                else:
                    print("equal")
                    return True

            else:
                break

        return False