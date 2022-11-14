class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        
        for row in range(m):
            for col in range(n):
                num = matrix[row][col]
                if not num:
                    for i in range(n):
                        if i <= col:
                            matrix[row][i] = 0
                        else:
                            if not matrix[row][i]:
                                continue
                            matrix[row][i] = "0"
                    for j in range(m):
                        if j <= row:
                            matrix[j][col] = 0
                        else:
                            if not matrix[j][col]:
                                continue
                            matrix[j][col] = "0"
                if num == "0":
                    num = 0
                