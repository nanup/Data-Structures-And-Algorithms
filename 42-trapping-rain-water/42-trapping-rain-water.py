class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        area = 0
        leftMax, rightMax = height[left], height[right]
        while left < right:
            if height[left] >= height[right]:
                right -= 1
                rightMax = max(rightMax, height[right])
                area += rightMax - height[right]
            else:
                left += 1
                leftMax = max(leftMax, height[left])
                area += leftMax - height[left]
        return area