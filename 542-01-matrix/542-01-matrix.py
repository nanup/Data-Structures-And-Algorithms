class Solution:
    def updateMatrix(self, matrix):
        rows = len(matrix)
        if rows == 0:
            return matrix
        cols = len(matrix[0])
        dist = [[float('inf') - 100000 for _ in range(cols)] for _ in range(rows)]

        # First pass: check for left and top
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    dist[i][j] = 0
                else:
                    if i > 0:
                        dist[i][j] = min(dist[i][j], dist[i - 1][j] + 1)
                    if j > 0:
                        dist[i][j] = min(dist[i][j], dist[i][j - 1] + 1)

        # Second pass: check for bottom and right
        for i in range(rows - 1, -1, -1):
            for j in range(cols - 1, -1, -1):
                if i < rows - 1:
                    dist[i][j] = min(dist[i][j], dist[i + 1][j] + 1)
                if j < cols - 1:
                    dist[i][j] = min(dist[i][j], dist[i][j + 1] + 1)

        return dist