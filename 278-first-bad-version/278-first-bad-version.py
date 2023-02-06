# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 0, n
        
        while left <= right:
            mid = (left + right) // 2
            
            isMidBad = isBadVersion(mid)
            
            if isMidBad:
                if not isBadVersion(mid - 1): return mid
                right = mid - 1
            else:
                left = mid + 1