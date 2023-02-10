class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 00 - 02
        # 01 - 12
        # 02 - 22
        
        # 10 - 01
        # 11 - 11
        # 12 - 21
        
        # 20 - 00
        # 21 - 10
        # 22 - 20
        
        #963
        #852
        #741
        
        for i in range(len(matrix)):
          for j in range(len(matrix) - i - 1):
            matrix[i][j], matrix[len(matrix) - j - 1][len(matrix) - i - 1] = matrix[len(matrix) - j - 1][len(matrix) - i - 1], matrix[i][j]
            
        for i in range(len(matrix) // 2):
          for j in range(len(matrix)):
            matrix[i][j], matrix[len(matrix) - i - 1][j] = matrix[len(matrix) - i - 1][j], matrix[i][j]
          