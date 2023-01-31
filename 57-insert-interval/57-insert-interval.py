class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0: return [newInterval]
        newIntervals = []
        start, end = 0, 1
        
        intervalStart, intervalEnd = newInterval[start], newInterval[end]
        
        for i in range(len(intervals)):
            interval = intervals[i]
            
            if interval[start] > intervalEnd:
                newIntervals.append([intervalStart, intervalEnd])
        
                for j in range(i, len(intervals)):
                    newIntervals.append(intervals[j])
                return newIntervals
            if interval[end] < intervalStart:
                newIntervals.append(interval)
                continue
                
            intervalStart = min(interval[start], intervalStart)
            intervalEnd = max(interval[end], intervalEnd)
            
        newIntervals.append([intervalStart, intervalEnd])
            
        return newIntervals