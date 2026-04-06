class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows = len(matrix)
        cols = len(matrix[0])
        
        # Create prefix sum table with extra row and column of 0s
        self.prefix = [[0] * (cols + 1) for _ in range(rows + 1)]
        
        for r in range(rows):
            for c in range(cols):
                self.prefix[r + 1][c + 1] = (
                    matrix[r][c]
                    + self.prefix[r][c + 1]    # top
                    + self.prefix[r + 1][c]    # left
                    - self.prefix[r][c]        # top-left (double counted)
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (
            self.prefix[row2 + 1][col2 + 1]       # whole rectangle
            - self.prefix[row1][col2 + 1]          # top strip
            - self.prefix[row2 + 1][col1]          # left strip
            + self.prefix[row1][col1]              # add back overlap
        )