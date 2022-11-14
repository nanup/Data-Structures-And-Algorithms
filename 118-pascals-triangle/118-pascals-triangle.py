class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for i in range(1, numRows + 1):
            row = [1] * i
            if i > 2:
                for j in range(1, i - 1):
                    row[j] = result[-1][j] + result[-1][j - 1]
            result.append(row)
        return result