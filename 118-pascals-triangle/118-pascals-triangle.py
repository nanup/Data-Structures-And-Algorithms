class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for n in range(1, numRows + 1):
            row = [1] * n
            for i in range(1, n - 1):
                row[i] = result[-1][i - 1] + result[-1][i]
            result.append(row)
        return result