import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        result = []
        for i in range(len(points)):
            point = points[i]
            x, y = point
            distance = math.sqrt(x ** 2 + y ** 2)
            
            heapq.heappush(minHeap, (distance, i))
            
        for _ in range(k):
            result.append(points[heapq.heappop(minHeap)[1]])
            
        return result