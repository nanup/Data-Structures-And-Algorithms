class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        configurations = []
        queenCols = set()
        positiveDiagonal = set()
        negativeDiagonal = set()
        
        board = [["."] * n for _ in range(n)]
        
        def backtrack(row):
            if row == n:
                copy = ["".join(row) for row in board]
                configurations.append(copy)
                return
            
            for col in range(n):
                if col in queenCols or \
                row + col in positiveDiagonal or \
                row - col in negativeDiagonal:
                    continue
                    
                queenCols.add(col)
                positiveDiagonal.add(row + col)
                negativeDiagonal.add(row - col)
                board[row][col] = "Q"
                
                backtrack(row + 1)
                
                queenCols.remove(col)
                positiveDiagonal.remove(row + col)
                negativeDiagonal.remove(row - col)
                board[row][col] = "."
                
        backtrack(0)
        return configurations
                