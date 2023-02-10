class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        mergedIntervals = []
        
        intervals.sort()
        
        start, end = 0, 1
        
        dummyStart, dummyEnd = intervals[0][start], intervals[0][end]
        
        for interval in intervals:
          if interval[start] <= dummyEnd:
            dummyEnd = max(dummyEnd, interval[end])
          else:
            mergedIntervals.append([dummyStart, dummyEnd])
            dummyStart, dummyEnd = interval[start], interval[end]
            
        mergedIntervals.append([dummyStart, dummyEnd])
        
        return mergedIntervals