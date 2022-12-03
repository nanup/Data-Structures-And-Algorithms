import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = []
        for num in nums:
            heappush(maxHeap, num)
            if len(maxHeap) > k:
                heappop(maxHeap)
            
        return heappop(maxHeap)