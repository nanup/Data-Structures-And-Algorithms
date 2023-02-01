from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        visited = set()
        
        result = mat.copy()
        
        q = deque()
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    q.appendleft((i, j))
                    visited.add((i, j))
                    
        while q:
            i, j = q.pop()
            
            for diff in [(0,1), (0, -1), (1, 0), (-1, 0)]:
                x, y = i + diff[0], j + diff[1]
                
                if x >= 0 and x < len(mat) and y >= 0 and y < len(mat[0]) and (x, y) not in visited:
                    result[x][y] = result[i][j] + 1
                    visited.add((x, y))
                    q.appendleft((x, y))
        
        return result