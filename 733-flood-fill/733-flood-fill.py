from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        stack = deque()
        
        stack.append([sr, sc])
        
        pixelColor = image[sr][sc]
            
        if pixelColor == color: return image
        
        while stack:
            i, j = stack.pop()
            
            if i > 0:
                if pixelColor == image[i - 1][j]:
                    stack.append([i - 1, j])
            if i < len(image) - 1:
                if pixelColor == image[i + 1][j]:
                    stack.append([i + 1, j])
                    
            if j > 0:
                if pixelColor == image[i][j - 1]:
                    stack.append([i, j - 1])
            if j < len(image[0]) - 1:
                if pixelColor == image[i][j + 1]:
                    stack.append([i, j + 1])
                    
            image[i][j] = color
            
        return image