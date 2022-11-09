class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                currNum = matrix[i][j]
                if currNum == 0:
                    for m in range(len(matrix)):
                        if matrix[m][j] == 0:
                            continue
                        if m <= i:
                            matrix[m][j] = 0
                        else:
                            matrix[m][j] = "0"
                    for n in range(len(matrix[0])):
                        if matrix[i][n] == 0:
                            continue
                        if n <= j:
                            matrix[i][n] = 0
                        else:
                            matrix[i][n] = "0"
                elif currNum == "0":
                    currNum = 0
                    
                        