class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        intervals.sort()
        start, end = 0, 1
        intStart = intervals[0][start]
        intEnd = intervals[0][end]
        for interval in intervals:
            if interval[start] <= intEnd:
                intStart = min(interval[start], intStart)
                intEnd = max(interval[end], intEnd)
            else:
                result.append([intStart, intEnd])
                intStart = interval[start]
                intEnd = interval[end]
        result.append([intStart, intEnd])
        return result
            