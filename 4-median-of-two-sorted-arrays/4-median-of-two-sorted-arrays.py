class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A
        half = (len(A) + len(B)) // 2
        
        left, right = 0, len(A) - 1
        
        while True:
            cutA = (left + right) // 2
            cutB = half - cutA - 2
            
            leftA = A[cutA] if cutA >= 0 else float(-math.inf)
            leftB = B[cutB] if cutB >= 0 else float(-math.inf)
            rightA = A[cutA + 1] if cutA < len(A) - 1 else float(math.inf)
            rightB = B[cutB + 1] if cutB < len(B) - 1 else float(math.inf)
            
            if leftA <= rightB and leftB <= rightA:
                if (len(A) + len(B)) % 2:
                    return min(rightA, rightB)
                else:
                    return ((max(leftA, leftB) + min(rightA, rightB)) / 2)
            if leftA > rightB:
                right = cutA - 1
            elif leftB > rightA:
                left = cutA + 1